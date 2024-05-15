import asyncio
import os
import sqlite3
from datetime import datetime

import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from openpyxl.workbook import Workbook

from database import create_database, update_database
from parser import get_exchange_rate

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("get_exchange_rate"))
async def get_exchange_rate_command(message: types.Message):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    conn = sqlite3.connect('exchange_rates.db')
    c = conn.cursor()
    c.execute("SELECT * FROM exchange_rates WHERE date=?", (date,))
    exchange_rates = c.fetchall()
    conn.close()

    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Дата'
    sheet['B1'] = 'Час'
    sheet['C1'] = 'Курс долара до гривні'
    for idx, rate_data in enumerate(exchange_rates, start=2):
        sheet[f'A{idx}'] = rate_data[0]  # Day
        sheet[f'B{idx}'] = rate_data[1]  # Time
        sheet[f'C{idx}'] = rate_data[2]  # Rate

    filename = f"exchange_rate_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    workbook.save(filename)

    await message.answer_document(FSInputFile(filename))

    os.remove(filename)


async def parsing() -> None:
    while True:
        update_database(get_exchange_rate())
        await asyncio.sleep(3600)   # 3600 sec = 1 hour


async def main() -> None:
    create_database()
    asyncio.create_task(parsing())
    await dp.start_polling(bot)


asyncio.run(main())
