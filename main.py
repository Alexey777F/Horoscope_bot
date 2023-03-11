import logging
from aiogram.utils import executor
import handlers
from config.config import dp
import datetime
from asyncio.exceptions import TimeoutError


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
while True:
    logger = logging.getLogger(__name__)
    try:
        executor.start_polling(dp, skip_updates=True, timeout=20)
    except TimeoutError as e:
        logger.error(datetime.datetime.now(), e)
        continue
