import csv
from bs4 import BeautifulSoup



with open(f"data/Maryland21220-2.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

csv_data = []
for el in soup.find_all("tr"):
    row = []
    for item in el.find_all("td"):
        row.append(item.text.strip())
    csv_data.append(row)


for row in csv_data:
    with open(f"data/Maryland21220-2.csv", "a", encoding="utf-8-sig", newline="") as csv_f:
        writer = csv.writer(csv_f, delimiter=';')
        writer.writerow(row)
