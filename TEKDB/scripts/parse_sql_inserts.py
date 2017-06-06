import sys
# IN = '../docs/Back_End_Dummy_Data_PGSQL.sql'
IN = sys.argv[1]
# OUT = 'insert.sql'
OUT = sys.argv[2]

with open(IN) as rf:
    with open(OUT, "w") as wf:
        for line in rf:
            if "DROP TABLE IF EXISTS" in line:
                line_split = line.split("\"")
                table_name = line_split[1]
                if ("Lookup" in table_name or "User" in table_name or "Citations" in table_name or table_name in ['Media', 'Locality']) and not table_name in ['LookupAuthorType']:
                    new_line = 'TRUNCATE TABLE "%s" CASCADE;\n' % table_name
                else:
                    new_line = 'TRUNCATE TABLE "%s";\n' % table_name
                wf.write(new_line)
            if "INSERT INTO \"" in line or "SELECT setval(" in line:
                wf.write(line)
