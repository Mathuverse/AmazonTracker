import requests
from bs4 import BeautifulSoup
import smtplib
MY_EMAIL="Mathudeals@gmail.com"
MY_PASS="ngzjeqhpuqfwbqja"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
import lxml

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=URL,headers=headers)

soup = BeautifulSoup(response.text,"lxml")

price=(float(soup.find(class_="a-offscreen").getText().replace("$","")))

if price < 50:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:

        connection.starttls()

        connection.login(MY_EMAIL,MY_PASS)

        connection.sendmail(

        from_addr=MY_EMAIL,

        to_addrs=MY_EMAIL,

        msg=f"Subject:Price Drop\n\nprice of item is {price}!!!"
    )