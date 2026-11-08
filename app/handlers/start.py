from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    await message.answer(
        f"Welcome, {message.from_user.first_name}!\n\n"
        "Your Telegram bot is running.\n"
        "Use /help to see available commands."
    )