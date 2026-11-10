FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      bash ca-certificates curl jq libwww-perl openssl \
      munin munin-node munin-plugins-extra && \
    rm -rf /var/lib/apt/lists/*

COPY munin.conf /etc/munin/munin.conf
COPY munin-node.conf /etc/munin/munin-node.conf
COPY plugin-conf.tekdb /etc/munin/plugin-conf.d/tekdb
COPY docker_stats /usr/share/munin/plugins/docker_stats
COPY entrypoint.sh /entrypoint.sh

RUN chmod 755 /usr/share/munin/plugins/docker_stats /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]