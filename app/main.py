import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from app.config import BOT_TOKEN

from app.handlers import (
    start,
    help,
    messages,
)


async def main():

    bot = Bot(token=BOT_TOKEN)

    # Register Telegram commands
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Show help"),
        BotCommand(command="about", description="About the bot"),
        BotCommand(command="messages", description="Message functionality"),
    ])

    dp = Dispatcher()

    # Register application routers
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(messages.router)

    logging.info("Starting Telegram bot...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    asyncio.run(main())