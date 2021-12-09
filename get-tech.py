import os

file = open("techs.txt", "r")
lines = file.readlines()

url = ""
tech = ""

for line in lines:
    values = line.split(" ")
    if len(values) >= 2:
        url = values[0]
        print(url)
        all_techs = values[1:]
        arr_techs = str(" ".join(all_techs)).split(",")

        for tech in arr_techs:
            tech_str = tech.replace("[", "").replace("]", "").replace("\n", "")
            print(url, tech_str)
            run = 'python3 insert-data.py -u "{}" -t "{}"'.format(url, tech_str)
            os.system(run)
    else:
        url = values[0]
        run = 'python3 insert-data.py -u "{}" -t ""'.format(url)
        os.system(run)
