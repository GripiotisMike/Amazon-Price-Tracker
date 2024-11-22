import lxml
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Amazon product URL (change it based on your product needs)
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Fetch product data
response = requests.get(url)
response.raise_for_status()
data = response.text

# Parse the HTML data
soup = BeautifulSoup(data, "lxml")
price = soup.select("div > span")
price = float(price[8].text.split("$")[1])  # Extract and convert price to float

# Check if price is below threshold
THRESHOLD_PRICE = 72
if price < THRESHOLD_PRICE:
    my_mail = os.getenv("EMAIL")  # Your email address
    my_pass = os.getenv("EMAIL_PASSWORD")  # Your email app password
    recipient = os.getenv("RECIPIENT_EMAIL")  # Recipient's email address

    # Send an email notification
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=recipient,
            msg=f"Subject:Price Alert for Instant Pot!\n\n"
                f"The price has dropped to ${price}.\n\n"
                f"Check it out here: {url}"
        )
    print(f"Email sent to {recipient}!")
else:
    print("Better luck next time!")
