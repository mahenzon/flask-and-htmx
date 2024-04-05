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

Этап 9:
- Добавление CSRF (из Flask-WTF) защиты
- Обработка формы Flask-WTF для добавления товара

Этап 10:
- Добавление заголовков `hx-headers`
- CSRF exempt

Этап 11:
- Удаление товара
- Выбор цели:
  - по ближайшему тегу: `hx-target="closest li"`
  - по ближайшему классу: `hx-target="closest .product-item"`
- Анимации:
  - Загрузка `.htmx-request`
  - Замена `.htmx-swapping`

Этап 12:
- Обновление товара:
  - PUT запрос
  - обработка ошибок (форма)

Этап 13:
- HTMX Push url - замена для истории браузера
- `hx-target="body"`
- `hx-confirm`

Этап 14:
- Автоматическая подгрузка в бесконечный список (с анимацией)
- `hx-trigger="revealed"`
