import sqlite3
import optparse


def menu():
    parser = optparse.OptionParser()
    parser.add_option(
        "-u", "--url", dest="url", help="Target url (ex. http://target-uri/)"
    )
    parser.add_option("-t", "--tech", dest="tech", help="Technology (ex. Imperva)")

    options, args = parser.parse_args()

    if not options.tech:
        options.tech = ""

    return options.url, options.tech.lower()


site, tech = menu()

con = sqlite3.connect("bbdata.db")
cur = con.cursor()

CHECK_IF_SITE_EXISTS = "SELECT id FROM sites WHERE site = '{}'"
CHECK_IF_TECHNOLOGY_EXISTS = "SELECT id FROM technologies WHERE technology = '{}'"
CHECK_IF_SITE_TECHNOLOGY_EXISTS = (
    "SELECT id FROM site_technology WHERE site_id = '{}' AND technology_id = '{}'"
)

INSERT_SITE = "INSERT OR IGNORE INTO sites(site) VALUES ('{}')"
INSERT_TECHNOLOGY = "INSERT OR IGNORE INTO technologies(technology) VALUES ('{}')"
INSERT_SITE_TECHNOLOGY = (
    "INSERT OR IGNORE INTO site_technology(site_id, technology_id) VALUES ('{}', '{}')"
)

cur.execute(CHECK_IF_SITE_EXISTS.format(site))
site_id = cur.fetchone()

if not site_id:
    cur.execute(INSERT_SITE.format(site))
    site_id = cur.lastrowid
else:
    site_id = site_id[0]

cur.execute(CHECK_IF_TECHNOLOGY_EXISTS.format(tech))
tech_id = cur.fetchone()

if not tech_id:
    cur.execute(INSERT_TECHNOLOGY.format(tech))
    tech_id = cur.lastrowid
else:
    tech_id = tech_id[0]

cur.execute(CHECK_IF_SITE_TECHNOLOGY_EXISTS.format(site_id, tech_id))
site_tech_id = cur.fetchone()

if not site_tech_id:
    cur.execute(INSERT_SITE_TECHNOLOGY.format(site_id, tech_id))
    site_tech_id = cur.lastrowid
else:
    site_tech_id = site_tech_id[0]

print(site_id, tech_id, site_tech_id)

con.commit()

con.close()
