import requests
from bs4 import BeautifulSoup
import json
import csv

LPF_Domain = ""

columns = ["position", "image", "name", "games", "goals", "points"]
standings = []

page = requests.get("https://lpf.ro/liga-1")
# print(page.content)
soup = BeautifulSoup(page.content, features="html.parser")
# table_parent = soup.find(id = "clasament_ajax_playoff")
# table = table_parent.find("table")
table = soup.find(id="clasament_ajax_playoff").find("table")
table_rows = table.find_all("tr", class_="echipa_row")

for table_row in table_rows:
    text_from_td_elements = [
        td for td in table_row.find_all("td") if "hiddenMobile" not in td.get("class", [])
    ]
    team_dict = {
        col: (data.text or data.find("img")["data-src"]) for col, data in zip(columns, text_from_td_elements)
    }
    standings.append(team_dict)

print(standings)

# Open and write to a json file
with open("standings.json", mode="w") as json_file:
    json.dump(standings, json_file, indent=2)

# Open and write to a csv file
with open("standings.csv", mode="w") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(columns)
    csv_write.writerows([team_data.values() for team_data in standings])
