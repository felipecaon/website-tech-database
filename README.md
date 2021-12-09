A simple concept to store websites with used technoogies altogether.

# Requirements

* Python3
* Sqlite

# Installation

```
sudo apt install python3
```

```
sudo apt install sqlite3
```

```
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

# Getting started

This repository comes with a pre-populated sqlite database called `bbdata.db`. In the case you want to create a new one from zero follow the steps:

1. Remove `bbdata.db`

```
rm bbdata.db
```

2. Run the initial script that build the default database structure.

```
python3 create-table.py
```

- `bbdata.db` filename is hardcoded within the script. This can be changed. But keep in mind the filename will have to be changed across all python files.

3. Get a list of websites with technologies

An example of the only accepted format can be found inside `techs.txt` file.
To achieve this format you need to probe a list of domains to httpx or nuclei using provided tech-detected.yml template and the resullt shall be the desired output.

```
cat domains.txt | httpx --tech-detect -nc > httpx_tech.json
```

**The output file name is required to be techs.txt.**

4. Populate the database

After having `httpx_tech.json` file you can run process_url_tech.py script

```
python3 process_url_tech.py
```

Wait for the script to stop and enjoy your populated dataset.


# Database Structure

TODO

# Access data

TODO

# Further implementations

-  insert-data currenly opens a new connection for each iteraction, which makes the process somewhat slower, it makes more sense to create a file with all queries file and then commit everything.
-  get-tech should not call insert-data from an os perspective.
-  expand database columns and add more information about domains.
-  pre-checks in create-table script  

# Contribute

PRs and issues are welcome.



 
