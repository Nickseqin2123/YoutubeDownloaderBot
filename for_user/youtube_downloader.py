import os

from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.chat_action import ChatActionSender

from downloaders.download import get_video
from keyboards.keyboard import button_for, menu
from pytube import YouTube


router = Router(name=__name__)
bot = Bot(token="6998969190:AAEn1jQ4TyBkx1Y9s1E-YqFZjXsUMS8QIiE")


class DownloadSelect(StatesGroup):
    sel = State()


@router.message(F.text == "Скачать видео с YouTube")
async def yt_do(message: Message, state: FSMContext):
    await message.answer(
        text="Отправь мне ссылку на видео",
        reply_markup=button_for()
    )
    await state.set_state(DownloadSelect.sel)


@router.message(F.text == "Главное меню")
async def go_to_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        return

    await state.clear()
    await message.answer(
        text="Мы в меню",
        reply_markup=menu()
    )


@router.message(DownloadSelect.sel)
async def get_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    data = await state.get_data()
    await state.clear()

    await summary(message, data, state)


async def summary(message: Message, data: dict, state: FSMContext):
    try:
        obj = YouTube(data['url'])
    except Exception:
        await message.answer(
            text="Ошибка. Вы ввели не URL.Введите корекктный URL видео"
        )
        await state.set_state(DownloadSelect.sel)
    else:
        await message.answer(
            text=f"Начало загрузки видео -> {obj.title}"
        )
        get_video(obj, message.from_user.id)
        await message.answer(
            text='Отправка видео...'
        )

        async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):
            await bot.send_video(chat_id=message.chat.id,
                                 video=FSInputFile(f"video_{message.from_user.id}.mp4"),
                                 reply_markup=menu())
            os.remove(f"video_{message.from_user.id}.mp4")