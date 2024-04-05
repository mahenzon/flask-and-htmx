# Flask ❤️ HTMX

URLs:
- https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/


Этап 1:
- Инициализация Flask приложения

Этап 2:
- Установка HTMX

Этап 3:
- Ping
  - on click
  - on shift + click
- Hover
- HTMX:
  - `hx-swap="outerHTML"`
  - `hx-trigger="mouseenter"`
  - `hx-trigger="click[shiftKey]"`

Этап 4:
- Clicker via HTMX

Этап 5:
- Embed clicker into index via HTMX

Этап 6:
- Handle HTMX boosts

Этап 7:
- Список товаров
- Создание через форму

Этап 8:
- Создание через HTMX форму + подгрузка списка
- Добавление через `hx-swap="beforeend"`
- Обработка out of band элементов
- Использование `hx-swap="none"`
- Возвращение нескольких кусков для замены: форма и oob-item
- Добавление CSRF (из Flask-WTF) защиты
