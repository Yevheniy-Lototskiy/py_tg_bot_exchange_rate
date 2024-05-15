import sqlite3
from datetime import datetime


def create_database():
    conn = sqlite3.connect('exchange_rates.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS exchange_rates
                 (date TEXT, time TEXT, rate REAL)''')
    conn.commit()
    conn.close()


def insert_exchange_rate(date, current_time, rate):
    conn = sqlite3.connect('exchange_rates.db')
    c = conn.cursor()
    c.execute("INSERT INTO exchange_rates VALUES (?, ?, ?)", (date, current_time, rate))
    conn.commit()
    conn.close()


def update_database(rate: float):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    insert_exchange_rate(date, current_time, rate)
