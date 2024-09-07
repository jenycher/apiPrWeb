import asyncio

import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from aiogram.types import Message

# Ваш токен от BotFather
TELEGRAM_TOKEN = '6745822426:AAFTc_HYlfpTsSQqDvp2qhrWG_BsRzQz8y0'

# URL для запроса данных с API
API_URL = 'https://api.coinex.com/v2/spot/ticker?market=BTCUSDT,LTCUSDT,BELlSCOINUSDT,DOGEUSDT'

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
   await message.answer("Привет! Я бот по курсам, нажми /kurs")

# Обработчик команды /kurs
@dp.message(Command("kurs"))
async def get_kurs(message: Message):
    try:
        # Отправляем запрос к API
        response = requests.get(API_URL)
        response.raise_for_status()

        # Получаем JSON ответ от API
        data = response.json()

        if data.get("code") == 0:
            # Формируем сообщение для отправки пользователю
            message_text = ""
            for market in data["data"]:
                market_name = market["market"]
                last_price = market["last"]
                message_text += f"{market_name}: {last_price}\n"

            # Отправляем сообщение пользователю
            await message.answer(message_text)
        else:
            await message.answer("Ошибка при получении данных с API")

    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки запросов
        await message.answer(f"Ошибка: {str(e)}")

async def main():
   await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
   asyncio.run(main())
