import json
import os
from os.path import exists

HTTPX_TECH_FILENAME = "httpx_tech.json"
NUCLEI_TECH_FILENAME = "nuclei_tech.json"


def insert_data(url: str, technology: str):
    run = f'python3 insert-data.py -u "{url}" -t "{technology.lower()}"'
    os.system(run)


def check_file_existence(filename: str):
    tech_exists = exists(filename)

    if not tech_exists:
        return f"{filename} not found"


def parse_json(scan_type: str, line):
    if scan_type == "httpx":
        json_data = json.loads(line)
        url = json_data.get("url")
        technologies = json_data.get("technologies")

        if technologies:
            for tech in technologies:
                print(url, tech.lower())
                insert_data(url, tech)
        else:
            print(url, "")
            insert_data(url, "")
    elif scan_type == "nuclei":
        json_data = json.loads(line)
        url = json_data.get("host")
        tech = json_data.get("matcher_name")

        if tech:
            print(url, tech.lower())
            insert_data(url, tech)
        else:
            print(url, "")
            insert_data(url, tech)
    else:
        return "Invalid scan_type"


def load_file(scan_type: str):
    if scan_type == "httpx":
        filename = HTTPX_TECH_FILENAME
    elif scan_type == "nuclei":
        filename = NUCLEI_TECH_FILENAME
    else:
        return "Invalid scan_type"

    check_file_existence(filename)

    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            if line != "\n":
                parse_json(scan_type, line)


load_file("nuclei")
load_file("httpx")
