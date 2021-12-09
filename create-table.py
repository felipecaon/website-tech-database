import sqlite3
con = sqlite3.connect('bbdata.db')
cur = con.cursor()

CREATE_SITES_TABLE = "CREATE TABLE sites(id INTEGER PRIMARY KEY, site VARCHAR);"
CREATE_TECHNOLOGIES_TABLE = "CREATE TABLE technologies(id INTEGER PRIMARY KEY, technology VARCHAR);"
CREATE_UNIQUE_INDEX_SITES_SITE = "CREATE UNIQUE INDEX sites_site ON sites(site);"
CREATE_UNIQUE_INDEX_TECHNOLOGIES_TECHNOLOGY = "CREATE UNIQUE INDEX technologies_technology ON technologies(technology);"
CREATE_SITE_TECHNOLOGY_TABLE = "CREATE TABLE site_technology(id INTEGER PRIMARY KEY, technology_id INT, site_id INT, CONSTRAINT fk_technology FOREIGN KEY(technology_id) REFERENCES technologies(id), CONSTRAINT fk_site FOREIGN KEY(site_id) REFERENCES sites(id));"

cur.execute(CREATE_SITES_TABLE)
cur.execute(CREATE_TECHNOLOGIES_TABLE)
cur.execute(CREATE_UNIQUE_INDEX_SITES_SITE)
cur.execute(CREATE_UNIQUE_INDEX_TECHNOLOGIES_TECHNOLOGY)
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute(CREATE_SITE_TECHNOLOGY_TABLE)

con.commit()

con.close()
