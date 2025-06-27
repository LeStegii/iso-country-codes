import csv
import sys

import requests
from bs4 import BeautifulSoup

# The url contains a header <h3> with id "Officially_assigned_code_elements" followed by a table
url = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException as e:
    raise Exception(f"Failed to connect to the URL: {e}")

soup = BeautifulSoup(response.text, "html.parser")

header = soup.find("h3", id="Officially_assigned_code_elements")
if not header:
    raise Exception("Could not find the <h3> with id 'Officially_assigned_code_elements'")

tbody = header.find_next("tbody")
if not tbody:
    raise Exception("Could not find a <tbody> following the header")

writer = csv.writer(sys.stdout)

for row in tbody.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) == 5:
        try:
            country_code = columns[0].text.strip()
            country_name = columns[1].text.strip()
            writer.writerow([country_code, country_name])
        except ValueError as e:
            print(f"Skipping row {columns} due to error: {e}", file=sys.stderr)
