#!/bin/bash
set -euo pipefail

WWW=/var/cache/munin/www

mkdir -p /run/munin "$WWW" /var/lib/munin /var/log/munin
chown -R munin:munin /run/munin /var/cache/munin /var/lib/munin /var/log/munin

# Basic-auth credentials for the dashboard 
#   nginx reads the htpasswd file from the shared volume
password=${MUNIN_PASSWORD:-}
if [ -z "$password" ]; then
  generated=/var/lib/munin/generated_password
  [ -s "$generated" ] || { openssl rand -hex 16 > "$generated"; chmod 600 "$generated"; }
  password=$(cat "$generated")
  echo "MUNIN_PASSWORD not set; using generated password stored in the munin volume at $generated"
fi
echo "${MUNIN_USER:-admin}:$(openssl passwd -apr1 -stdin <<< "$password")" > "$WWW/.htpasswd"
chmod 644 "$WWW/.htpasswd"

rm -f /etc/munin/plugins/*
munin-node-configure --shell --suggest 2>/dev/null | sh || true
ln -sf /usr/share/munin/plugins/nginx_status /etc/munin/plugins/nginx_status
ln -sf /usr/share/munin/plugins/nginx_request /etc/munin/plugins/nginx_request
ln -sf /usr/share/munin/plugins/docker_stats /etc/munin/plugins/docker_cpu
ln -sf /usr/share/munin/plugins/docker_stats /etc/munin/plugins/docker_memory

trap 'kill 0' EXIT

munin-node &

(
  sleep 5
  while true; do
    su -s /bin/sh munin -c /usr/bin/munin-cron || echo "munin-cron failed" >&2
    sleep 300
  done
) &

wait -n
exit 1