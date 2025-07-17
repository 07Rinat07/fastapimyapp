<div align="center">
  <img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" width="600" height="300"/>
</div>

### Реализация простейшего API на базе FastAPI, создание базы и таблицы внутри нее при помощи SQLAlchemy, описание схемы данных и валидировать их при помощи Pydantic.

### Подготовка окружения (выбрать одну из трех)
* python -m venv venv
* python3 -m venv venv
* py -m venv venv
### Установка библиотек (установить необходимые библиотеки с помощью следующей команды:)
* pip install fastapi uvicorn pydantic aiosqlite sqlalchemy
* (Если у вас возникли конфликты версий библиотек, обратитесь к их документации или к паку версий, использующемся в проекте: aioqlite==0.19.0 fastapi==0.109.0 pydantic==2.5.3 SQLAlchemy==2.0.25 uvicorn==0.25.0)
#### Рассмотрим вкратце их предназначение.
* (FastAPI — это популярный асинхронный фреймворк, позволяющий быстро писать API.
Pydantic — это быстрая и обширная библиотека для валидации и сериализации данных. Она входит в список основных зависимостей FastAPI, так как они тесно связаны друг с другом.
Uvicorn — библиотека, позволяющая запустить свой собственный веб-сервер.
SQLAlchemy — самая известная библиотека для работы с реляционными базами данных через Python.
Aiosqlite — асинхронный драйвер для работы легковесной базы данных SQLite, которую можно создать и распространять как обычный файл.)
### Запуск веб-сервер Uvicorn (перейти в браузере по адресу http://127.0.0.1:8000 или http://localhost:8000):
*  .\venv\Scripts\activate   
* uvicorn main:app --reload
* (Работа Uvicorn в связке с FastAPI выглядит следующим образом:
наш запрос поступает в Uvicorn;
Uvicorn передает этот запрос в FastAPI;
FastAPI запускает код, который мы написали, и возвращает ответ Uvicorn-у:
return {«data»: «Hello World»};
Uvicorn возвращает ответ нам. Если зайти по адресу http://localhost:8000/docs, то мы увидим удобный интерфейс для тестирования наших эндпоинтов. 
#### Со всего проекта берет все установленные зависимости в файл для последующей установки например через Docker.
* pip freeze > requirements.txt

### Загрузка и разворачивание через Докер, проекта на облачный сервер
* создать сервер и авторизоваться по SSH:

### Установить необходимые зависимости: git и Docker.
1. sudo apt-get update
2. sudo apt-get install git
3. sudo apt-get update
4. sudo apt-get install ca-certificates curl gnupg
5. sudo install -m 0755 -d /etc/apt/keyrings
6. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
7. sudo chmod a+r /etc/apt/keyrings/docker.gpg
8. echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
 $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
9. sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
10. sudo apt-get update
11. sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
### После установки git и Docker необходимо клонировать созданный ранее репозиторий:
* git clone REPO_URL.git
* или использовать готовый репозиторий с помощью команды:
* git clone https://git@github.com:07Rinat07/fastapimyapp.git
### После клонирования проекта необходимо перейти в папку с проектом:
* cd <название_папки>
* И запустить команду для сборки образа fastapi_app и запуска контейнера на порту 80:
* docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app
* после этого приложение доступно по IP-адресу сервера