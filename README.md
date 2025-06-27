# 🌍 ISO Scraper
A very simple script for scraping the current list of ISO 3166-1 alpha-2 country codes and their names from [Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).

As this scrapes Wikipedia, which is always evolving, the script may break if the structure of the page changes.

## Installation and Usage

```bash
pip install -r requirements.txt
python3 iso_scraper.py > iso_codes.csv
```

## Output
The script will print any output to STDOUT, which can be redirected to a file. The output will be in CSV format with the following columns:

```csv
AD,Andorra
AE,United Arab Emirates
AF,Afghanistan
AG,Antigua and Barbuda
AI,Anguilla
...
```
