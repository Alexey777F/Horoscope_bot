from aiohttp import web
from dotenv import load_dotenv, find_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

bot_token = getenv("TG_TOKEN")
ngrok_tunnel_url = getenv("NGROK_TUNNEL_URL")
webhook_path = f"/{bot_token}"
webhook_url = f"{ngrok_tunnel_url}{webhook_path}"

bot = Bot(token=bot_token)
Bot.set_current(bot)
dp = Dispatcher(bot=bot)
app = web.Application()

from handlers import start_handler, zodiakal_handler, chinese_handler, japanese_handler, druid_handler, compatibility_handler, help_handler, echo_handler
# from handlers.start_handler import *
# from handlers.zodiakal_handler import *
# from handlers.chinese_handler import *
# from handlers.japanese_handler import *
# from handlers.compatibility_handler import *
# from handlers.druid_handler import *
# from handlers.help_handler import *
# from handlers.echo_handler import *

async def set_webhook():
    webhook_uri = f'{webhook_url}'
    await bot.set_webhook(
        webhook_uri
    )


async def on_startup(_):
    await set_webhook()


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index + 1:]
    if token == bot_token:
        update = types.Update(**await request.json())
        print(update)
        await dp.process_update(update)
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post(webhook_path, handler=handle_webhook)

if __name__ == "__main__":
    app.on_startup.append(on_startup)
    web.run_app(app, host='0.0.0.0', port=8081)