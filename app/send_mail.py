from database import get_last_price
import smtplib
import email.message
from os import getenv
from dotenv import load_dotenv

load_dotenv()
password = getenv("PASSWORD")
target = getenv("TARGET_EMAIL")
myemail = getenv("YOUR_EMAIL")

def build_email(prices: dict) -> str:

    date = prices.get("date")
    
    return f"""
    <h1><b>Preços do kindle</b></h1>
    <p><b>Kindle 11:</b> R$ {prices.get("kindle11")}</p>
    <p><b>Kindle Paperwhite:</b> R$ {prices.get("paperwhite")}</p>
    <p><b>Kindle Paperwhite Signature Edition:</b> R$ {prices.get("paperwhiteSE")}</p>
    <p><b>Kindle Oasis:</b> R$ {prices.get("oasis")}</p>
    <br>
    <br>
    <p><i>Ultima atualização {date.day}/{date.month}/{date.year} às {date.hour}:{date.minute}:{'0' if date.second < 10 else ''}{date.second}</i></p>
    """

print(build_email(get_last_price()))

def send_mail(your_email, to, password):
    msg = email.message.Message()
    msg['Subject'] = "Preço do Kindle hoje"
    msg["From"] = your_email
    msg["To"] = to
    msg.add_header("Content-Type","text/html")
    msg.set_payload(build_email(get_last_price()))

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()

    s.login(msg["From"], password)
    s.sendmail(msg['From'], [msg["To"]], msg.as_string().encode('utf-8'))
    print("Email sent!")

try:
    send_mail(myemail,target,password)
except:
    print("não foi possível enviar o email")