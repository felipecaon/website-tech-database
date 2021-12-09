import os
import json

with open("techs.json") as file:
    data = json.load(file)

    for url, techs in data['technologies'].items():
        print(f">>> Inserting technologies for {url}")

        if not techs:
            print("No tech found to insert, skipping...")
            continue

        for tech in techs:
            print(f"Inserting {tech}...")

            run = f'python3 insert-data.py -u "{url}" -t "{tech}"'
            os.system(run)

        print()
