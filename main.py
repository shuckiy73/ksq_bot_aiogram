from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from utils.commands import set_commands


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv("ADMIN_ID")

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Я запустил бота')

    dp.startup.register(start_bot)


async def start():
    await  set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

        if __name__ == '__main__':
            asyncio.run(start)
