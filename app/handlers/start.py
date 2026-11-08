from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.services.user_service import UserService

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    response = UserService.get_welcome_message(
        message.from_user.first_name
    )

    await message.answer(response)