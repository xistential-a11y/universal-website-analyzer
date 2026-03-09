import requests
from bs4 import BeautifulSoup
import pandas as pd

url = input("Enter website URL: ")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Page title
title = soup.title.string if soup.title else "No Title"

# Headings
headings = []
for tag in soup.find_all(["h1","h2","h3"]):
    headings.append(tag.text.strip())

# Links
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

data = {
    "Page Title": [title]*max(len(headings),len(links)),
    "Headings": headings + [""]*(max(len(headings),len(links))-len(headings)),
    "Links": links + [""]*(max(len(headings),len(links))-len(links))
}

df = pd.DataFrame(data)

df.to_excel("website_analysis.xlsx", index=False)

print("Analysis complete. Data saved to website_analysis.xlsx")
import os
print(os.getcwd())