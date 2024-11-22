# Amazon Price Tracker

A Python script that tracks the price of a specific product on Amazon and sends an email alert if the price drops below a specified threshold.

---

## Features
- 💰 **Price Tracking**: Monitors the price of a product on Amazon.
- 📧 **Email Alerts**: Sends a notification to your email when the price falls below a set value.

--- 

## Installation

1. Clone the repository

2. Install dependencies
- Python 3.6 or higher
- requests
- beautifulsoup4
- lxml
- python-dotenv

3. Modify the .env file to suit your needs

---

## Usage

1. Update the url variable in main.py with the Amazon product URL you want to track.

2. Set the price threshold by modifying THRESHOLD_PRICE

3. Run the script: python main.py

---

## Note 

- The script uses an SMTP server to send emails. Gmail users must generate an App Password to use this script.
- Make sure to comply with Amazon's web scraping policies.
