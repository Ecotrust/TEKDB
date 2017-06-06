import os
import sys
if not len(sys.argv) == 2:
    print("import_sql takes 1 additional argument: the sql file import. %d given" % int(len(sys.argv)-1))
    for arg in sys.argv:
        print(arg)
    sys.exit(2)

infile = sys.argv[1]
insert_script = 'insert.sql'

print("Generating insert script")
parsing_script = os.path.join('.', 'parse_sql_inserts.py')
os.system("python %s %s %s" % (parsing_script, infile, insert_script))

print("Reverting migrations")
manage_py = os.path.join('..', 'manage.py')
os.system("%s migrate --fake TEKDB zero" % manage_py)

print("Deleting migration files...")
from pathlib import Path
migrations_path = os.path.join('..','TEKDB','migrations')
migrations = Path(migrations_path)
migration_files = [x for x in migrations.iterdir() if not x.name == '__init__.py' and not x.is_dir()]
for migration_file in migration_files:
    try:
        os.remove(str(migration_file))
        print('%s deleted' % migration_file.name)
    except OSError as e:
        pass

print("Dropping Database")
import psycopg2
dbname = 'tekdb'
conn_psql = psycopg2.connect("dbname=postgres user=postgres")
cur_psql = conn_psql.cursor()
conn_psql.set_isolation_level(0)
cur_psql.execute('DROP DATABASE if exists %s;' % dbname)
print("Recreating Database")
cur_psql.execute('CREATE DATABASE %s;' % dbname)
cur_psql.close()
conn_psql.close()

print("Making updated migration files")
os.system("%s makemigrations" % manage_py)

print("Migrating database")
os.system("%s migrate" % manage_py)

print("Transferring old data into new database")
from subprocess import Popen, PIPE

out = open('import_output.txt', 'w')
sys.stdout = out
error = open('import_error.txt', 'w')
sys.stderr = error

p = Popen(['psql', '-U', 'postgres', '-d', dbname, '-f', insert_script], stdout=PIPE, stderr=PIPE)
p.wait()
p = Popen(['psql', '-U', 'postgres', '-d', dbname, '-f', insert_script], stdout=PIPE, stderr=PIPE)
p.wait()
p = Popen(['psql', '-U', 'postgres', '-d', dbname, '-f', insert_script], stdout=out, stderr=error)
# p.wait()
