 # Goroscope_bot
 ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/6.png)
 * Это интересный Гороскоп бот в котором есть несколько разделов, Зодиакальный, Китайсикй, Японский, 
   Гороскоп друидов и гороскоп Совместимости по знакам зодиака. 
 ___
 * This is an interesting Horoscope bot in which there are several sections, Zodiac, Chinese, Japanese,
   Horoscope of druids and horoscope of Compatibility according to the signs of the zodiac.
   
## Технологии - Technologies
 * Docker-compose
 * Python(3.9);
 * Pillow(v. 9.4.0)
 * requests(v. 2.28.2)
 * aiogram(v. 2.25.1)
 * python-dotenv(v. 0.21.1)
 * python-telegram-bot-pagination(v. 0.0.2)
 * asyncio(v. 3.4.3)
 * aiohttp(v.3.8.6)
   
## Токены - Tokens
 * Создайте бота в телеграм с помощью BotFather и получите персональный токен.
 ___
 * Create a telegram bot with BotFather and get a personal token.

## Простой запуск - Simple start
 * Необходимо скопировать все содержимое репозитория в отдельный каталог.
 * Установите виртульное окружение на вашей ОС, на Mac OS python3 -m venv my_env
 * Активируйте виртульаное окружение на вашей ОС, на Mac OS source my_env/bin/activate
 * Установить все библиотеки из requirements.txt 
 * Важно! Установить именно те версии которые указаны в requirements.txt иначе возможны ошибки при работе бота.
 * Откройте файл .env и заполните токен.
 * Запустите файл main.py
 ___
 * It is necessary to copy all important repositories to a separate directory.
 * Install a virtual environment on your OS, on Mac OS python3 -m venv my_env
 * Activate the virtual environment in your OS, in the Mac OS source my_env/bin/activate.
 * Install all libraries from the requirements.txt file.
 * Important! Install exactly the version specified in the require.txt file, otherwise errors may occur when the bot operates.
 * Open the .env file and fill in token from bot.
 * Run main.py.

 
## Установка с помощью Docker-compose и asyncio(polling) - Install with Docker-compose and asyncio(polling)
 * Установите Docker Desktop под вашу ОС
 * Необходимо скопировать все содержимое репозитория в отдельный каталог.
 * Установите виртульное окружение на вашей ОС, на Mac OS python3 -m venv my_env
 * Активируйте виртульаное окружение на вашей ОС, на Mac OS source my_env/bin/activate
 * Установить все библиотеки из requirements.txt 
 * Важно! Установить именно те версии которые указаны в requirements.txt иначе возможны ошибки при работе бота.
 * Откройте файл .env и заполните необходимыми данными.
 * Запустите сборку образа и создания контейнера с помощью команды docker-compose up --build
 * Бот работает из контейнера
 ___
 * Install Docker Desktop on your OS
 * It is necessary to copy all important repositories to a separate directory.
 * Install a virtual environment on your OS, on Mac OS python3 -m venv my_env
 * Activate the virtual environment in your OS, in the Mac OS source my_env/bin/activate.
 * Install all libraries from the requirements.txt file.
 * Important! Install exactly the version specified in the require.txt file, otherwise errors may occur when the bot operates.
 * Open the .env file and fill in the reporting data.
 * Start building the image and creating the container using the docker-compose up --build command.
 * Bot runs from a container
   
## Установка с помощью Docker-compose и webhooks - Install with Docker-compose and webhooks
 * Установите Docker Desktop под вашу ОС
 * Необходимо скопировать все содержимое репозитория в отдельный каталог.
 * Установите виртульное окружение на вашей ОС, под Mac OS python3 -m venv my_env
 * Активируйте виртульаное окружение на вашей ОС, под Mac OS source my_env/bin/activate
 * Установить все библиотеки из requirements.txt 
 * Важно! Установить именно те версии которые указаны в requirements.txt иначе возможны ошибки при работе бота.
 * Скопируйте содержимое файла main_webhooks.py и вставьте его в файл main.py
 * Установите на вашем устройстве прокси сервер ngrok под Mac OS brew install ngrok/ngrok/ngrok
 * Запустите ngrok с помощью команды ngrok http 8081 - запускаете проксирование на тот порт на котором работает Ваше приложение!
 * Откройте файл .env и заполните необходимыми данными токеном с бота и полным url адресом вашего ngrok сервера
 * Вот пример url адреса сервера ngrok https://9acc-2a00-1370-818a-4905-b91e-e9db-441d-4e96.ngrok.io
 * Запустите сборку образа и создания контейнера с помощью команды docker-compose up --build
 * Бот работает из контейнера
___
 * Install Docker Desktop on your OS
 * It is necessary to copy all important repositories to a separate directory.
 * Install a virtual environment on your OS, on Mac OS python3 -m venv my_env
 * Activate the virtual environment in your OS, in the Mac OS source my_env/bin/activate.
 * Install all libraries from the requirements.txt file.
 * Important! Install exactly the version specified in the require.txt file, otherwise errors may occur when the bot operates.
 * Copy the contents of the main_webhooks.py file and paste it into the main.py file
 * Install ngrok proxy server on your device under Mac OS brew install ngrok/ngrok/ngrok
 * Run ngrok using the command ngrok http 8081 - start proxying on the port on which your application is running!
 * Open the .env file and fill in the necessary data with the token from the bot and the full url address of your ngrok server
 * Here is an example of the ngrok server url https://9acc-2a00-1370-818a-4905-b91e-e9db-441d-4e96.ngrok.io
 * Start building the image and creating the container using the command docker-compose up --build
 * Bot runs from a container
 * 
## Как работает - How does it works
  * Примеры работы бота 
  * Examples of how the bot works
  ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/1.png)
  ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/2.png)
  ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/3.png)
  ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/4.png)
  ![horoscope_bot](https://github.com/Alexey777F/Horoscope_bot/blob/master/5.png)
