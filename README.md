# Телеграм бот
## Команда №9

---------
## Описание работы

Телеграм бот с заданным функционалом:

1) Калькулятор
2) Просмотр погоды
3) Перевод текста
4) Мем дня

### Описание функций

<ul class="functions">
<li style="list-style-type: decimal;">Калькулятор</li>
   Операции, которые могут быть выполнены
   <ul class="operations">
   <li style="list-style-type: circle;">сложение (+)</li>
   <li style="list-style-type: circle;">вычитание (-)</li>
   <li style="list-style-type: circle;">умножение (*)</li>
   <li style="list-style-type: circle;">деление (/)</li>
   <li style="list-style-type: circle;">возведение в степень (^)</li>
   </ul>
<li style="list-style-type: decimal;">Просмотр погоды</li>
   Используется сайт OpenWeatherMap и библиотека request
<li style="list-style-type: decimal;">Перевод текста</li>
    Перевод текста осуществляется с помощью библиотеки googletrans. Язык, с которого переводится - любой, выходной язык - английский.
<li style="list-style-type: decimal;">Мем дня</li>
    Самая интересная часть проекта. Библиотеки для поиска случайных мемов найти сложно, так что в качестве источника был взят Reddit. Используется библиотека PRAW и <a href="https://www.reddit.com/r/ProgrammerHumor/">r/ProgrammerHumor</a>
</ul>

---------

### Начало работы:

<ul class="start_working">
<li><b>Скачивание</b></li>
    <code>git clone https://github.com/Miffle/Practice.git</code>
<li style="margin-top: 20px"><b>Установка библиотек</b></li>
    <code>pip install -r requirements.txt</code>
<li style="margin-top: 20px"><b>Создание файла INFO.py</b></li>
   Файл хранится в папке "bot_components" и содержит такой код: <br> `TOKEN = "Тут ваш токен"`
<li style="margin-top: 20px"><b>Запуск бота</b></li>
    <code>python main.py</code>
</ul>