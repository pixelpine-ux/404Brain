from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("messages"))
async def messages_handler(message: Message):
    await message.answer(
        "You can send me ordinary text messages "
        "and I'll process them here."
    )


@router.message()
async def unknown_message_handler(message: Message):
    await message.answer(
        "I don't understand that message yet.\n"
        "Use /help to see available commands."
    )