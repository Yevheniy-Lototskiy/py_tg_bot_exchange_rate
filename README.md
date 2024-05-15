# USD to UAH Exchange Rate Monitor Bot

## Description
This project is a Telegram bot designed to monitor the exchange rate of the US Dollar (USD) to Ukrainian Hryvnia (UAH).
It fetches the exchange rate data from Google Finance and stores it in a SQLite database. 
Users can query the bot using the `/get_exchange_rate` command to receive an Excel file with the exchange rate data for the current date.

## Features
- Fetches exchange rate data from Google Finance.
- Stores exchange rate data in a SQLite database.
- Provides users with the ability to query the exchange rate for the current date.
- Generates an Excel file with exchange rate data for the current date.

## Technologies Used
- Python 3
- aiogram (for Telegram bot functionality)
- requests (for making HTTP requests)
- BeautifulSoup4 (for web scraping)
- SQLite3 (for local database storage)
- openpyxl (for Excel file generation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yevheniy-Lototskiy/py_tg_bot_exchange_rate.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a Telegram bot and obtain the API token.
4. Update the `config.py` file with your Telegram bot API token.
5. Run the `telegram_bot.py` script to start the bot.

## Usage
1. Start the bot by running the `telegram_bot.py` script.
2. Send the `/get_exchange_rate` command to the bot to receive the exchange rate data for the current date.

## Contributing
Contributions are welcome! Please feel free to submit any issues or pull requests.
