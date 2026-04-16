#added notes
import requests
from bs4 import BeautifulSoup
import time

while True:
    print("Comparing Budget with price...")
    url = "https://www.interdiscount.ch/de/product/meta-vr-brille-meta-quest-3-512-gb-0014093649?srsltid=AfmBOop7zncd6uhhiDAvD049Rfw2QrhOhi8GVvy1Ofzz6bU_4OFl0NBD"
    header_data = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "de-CH,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.google.com/"
    }
    answer = requests.get(url, headers=header_data)
    soup = BeautifulSoup(answer.text, "html.parser")

    price_element = soup.find("span", class_="inline-flex")

    price_text = price_element.get_text()

    price_num = float(price_text)

    
    with open("budget.txt", "r") as doc:
        my_budget = float(doc.read().strip())

    print(f"Current Budget: {my_budget}")

    if price_num <= my_budget:
        print("Price is good!")
    else: print("Too expensive, keep waiting.")
    time.sleep(1800)

