import logging
import asyncio


from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters.command import CommandStart

from main_router import router as main_router
from keyboards.keyboard import menu


dp = Dispatcher()
dp.include_router(
    main_router
)
bot = Bot(token="6998969190:AAEn1jQ4TyBkx1Y9s1E-YqFZjXsUMS8QIiE")


@dp.message(CommandStart())
async def starting(message: Message):
    await message.answer(
        text="Привет, я бот, который позволяет скачать видео с YouTube по ссылке.",
        reply_markup=menu()
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())