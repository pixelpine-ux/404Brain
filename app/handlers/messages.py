from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def unknown_message_handler(message: Message):

    await message.answer(
        "I don't understand that message yet.\n"
        "Use /help to see available commands."
    )