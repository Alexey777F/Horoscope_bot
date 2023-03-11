import requests
import re
import logging
from typing import Any, List


def get_url(prediction, sign, date):
    url = f"https://horo.mail.ru/{prediction}/{sign}/{date}/"
    return url


def get_response(url) -> Any:
    """Функция которая возвращает ответ от https://horo.mail.ru/"""
    logger = logging.getLogger(__name__)
    try:
        response = requests.get(url, timeout=10)
        text = response.content.decode('utf8')
        if response.status_code == requests.codes.ok:
            return text
        else:
            return None
    except requests.exceptions.RequestException as exc:
        logger.error(exc, exc_info=exc)


def get_data(get_response) -> List:
    logger = logging.getLogger(__name__)
    try:
        our_data_text = re.findall(r'<p>([^<]+)</p>', get_response)
        return our_data_text
    except KeyError as exc:
        logger.error(exc, exc_info=exc)