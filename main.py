from handlers import start_handler, zodiakal_handler, chinese_handler, japanese_handler, druid_handler, compatibility_handler, help_handler, echo_handler
from config.config import dp
import asyncio
import logging


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")

