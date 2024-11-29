import os
import smtplib
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# product_url = input("Enter the product URL to check price history: ")
# target_price = input("Enter your target price: ")
target_price = 60000

product_url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_7?crid=2E3FJ9O2SONI0&dib=eyJ2IjoiMSJ9.Iz6876S7V6F-IKK7yCy4IZ94NM-KxFUokpFKjuysz2csXhAsdiJE0U4jyuZnwZxpOhk6_Cj1cTD9ueLs2BydRKumjgAizrpd6F9b-2ZsWPA9pCjWbYSoLBYG8GNrYKM7DJmGph4wo3U0pD_QbG0pAincGx-ncuLa0MOYvKkZE4OgI4ZHPYxM6DPIfc1B-QOTrnHL4tENXWLZocybrm3akCB41F0cZdVX7JMVj9lm-jc.rzezjZ1ZcyDL6IN47VaJMIfCMD9xzp4HjpN_goJzIB4&dib_tag=se&keywords=laptop&qid=1732735960&sprefix=lapto%2Caps%2C269&sr=8-7"
email_id = os.environ.get("EMAIL_ID")
password = os.environ.get("PASSWORD")


def send_mail(price):
    message = f"Item Price Down!\nBuy your at just {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_id,password=password)
        connection.sendmail(
            from_addr=email_id,
            to_addrs="ayush0187cse@outlook.com",
            msg= f"Subject:Alert\n{message}"
        )
        print("Email Sent!")



headers  = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(url=product_url,headers=headers)
contents = response.text

if response.status_code ==200:
    soup = BeautifulSoup(contents,"html.parser")
    soup.prettify()
    price = soup.find_all(name="span",class_ = "a-price-whole")
    # print(price)
    if price:
        price = int(price.text.replace(",", "").strip("."))
        if price<target_price:
            send_mail(price)
            



