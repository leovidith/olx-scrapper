import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("li", {"data-aut-id": "itemBox"})

with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])

    for item in items:
        title_tag = item.find("span", {"data-aut-id": "itemTitle"})
        price_tag = item.find("span", {"data-aut-id": "itemPrice"})
        link_tag = item.find("a", href=True)

        if title_tag and price_tag and link_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.olx.in" + link_tag["href"]
            writer.writerow([title, price, link])
print("Data has been written to olx_car_covers.csv")