from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):

    await message.answer(
        "Available commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show available commands\n"
        "/about - About this bot\n"
        "/messages - Message functionality"
    )


@router.message(Command("about"))
async def about_handler(message: Message):

    await message.answer(
        "A modular Telegram bot built with Python "
        "and aiogram 3."
    )