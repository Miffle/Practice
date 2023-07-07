# Телеграм бот команды №9

## Описание работы

Телеграм бот с заданным функционалом:

1) Калькулятор
2) Просмотр погоды
3) Перевод текста
4) Мем дня

### Описание функций

<ul class="functions">
<li>Калькулятор</li>
   Операции, которые могут быть выполнены
   <ul class="operations">
   <li>сложение (+)</li>
   <li>вычитание (-)</li>
   <li>умножение (*)</li>
   <li>деление (/)</li>
   <li>возведение в степень (^)</li>
   </ul>
<li>Просмотр погоды</li>
   Используется сайт OpenWeatherMap и библиотека request
<li>Перевод текста</li>
    Перевод текста осуществляется с помощью библиотеки googletrans. Язык, с которого переводится - любой, выходной язык - английский. Максимальный размер текста - 2999 символов.
<li>Мем дня</li>
    Самая интересная часть проекта. Библиотеки для поиска случайных мемов найти сложно, так что в качестве источника был взят Reddit. Используется библиотека PRAW и <a href="https://www.reddit.com/r/ProgrammerHumor/">r/ProgrammerHumor</a>
</ul>

### Начало работы:

<ul class="start_working">
<li><b>Скачивание</b></li>
    <code>git clone https://github.com/Miffle/Practice.git</code>
<li><b>Установка библиотек</b></li>
    <code>pip install -r requirements.txt</code>
<li><b>Создание файла INFO.py</b></li>
   Файл хранится в папке "bot_components" и содержит такой код: <br> <code>TOKEN = "Тут ваш токен"</code>
<li><b>Создание файла REDDIT_INFO.py</b></li>
    Файл хранится в папке "Functions/memes" и содержит такой код:
<pre>import praw
reddit = praw.Reddit(
    user_agent="*******",
    client_id='************',
    client_secret='*******')
</pre>
Чтобы получить все эти данные: <a href="https://praw.readthedocs.io/en/stable/getting_started/quick_start.html">Документация PRAW</a>
<li><b>Создание базы данных</b></li>
   В директории проекта создаём sqlite базу данных с названием "identifier.sqlite" и добавляем таблицу <br>
<pre>CREATE TABLE commands 
(id           integer
        constraint commands_pk
            primary key autoincrement,
    user_id      integer,
    used_command text,
    user_text    text,
    reply_text   text
)</pre>
<li><b>Запуск бота</b></li>
    <code>python main.py</code>
</ul>