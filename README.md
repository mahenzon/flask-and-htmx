# Flask ❤️ HTMX

## URLs
- https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/
- https://htmx.org/essays/hateoas/#:~:text=Hypermedia%20as%20the%20Engine%20of,provide%20information%20dynamically%20through%20hypermedia.
- https://steveklabnik.com/writing/nobody-understands-rest-or-http
- https://steveklabnik.com/writing/some-people-understand-rest-and-http

### HTTP
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

### HTMX
- https://htmx.org/
- https://htmx.org/docs/
- https://htmx.org/examples/animations/
- https://htmx.org/attributes/hx-trigger/
- https://htmx.org/attributes/hx-target/
- https://htmx.org/attributes/hx-boost/
- https://htmx.org/attributes/hx-post/
- https://htmx.org/attributes/hx-swap-oob/
- https://htmx.org/attributes/hx-swap/
- https://htmx.org/attributes/hx-headers/
- https://htmx.org/attributes/hx-indicator/
- https://htmx.org/attributes/hx-request/
- https://htmx.org/attributes/hx-push-url/
- https://htmx.org/attributes/hx-confirm/

### Flask
- https://flask.palletsprojects.com/en/3.0.x/
- https://jinja.palletsprojects.com/en/3.1.x/templates/
- https://flask-wtf.readthedocs.io/en/1.2.x/
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#javascript-requests
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#exclude-views-from-protection

### Static
- https://freesvg.org/trash-can-icon
- https://www.svgbackgrounds.com/elements/animated-svg-preloaders/


Этап 1:
- Инициализация Flask приложения
- https://flask.palletsprojects.com/en/3.0.x/
- https://jinja.palletsprojects.com/en/3.1.x/templates/

Этап 2:
- Установка HTMX
- https://htmx.org/
- https://htmx.org/docs/

Этап 3:
- Ping
  - on click
  - on shift + click
- Hover
- HTMX:
  - `hx-swap="outerHTML"`
  - `hx-trigger="mouseenter"`
  - `hx-trigger="click[shiftKey]"`
- https://htmx.org/attributes/hx-trigger/

Этап 4:
- Clicker via HTMX
- https://htmx.org/attributes/hx-post/
- https://htmx.org/attributes/hx-swap/

Этап 5:
- Embed clicker into index via HTMX

Этап 6:
- Handle HTMX boosts
- https://htmx.org/attributes/hx-boost/

Этап 7:
- Список товаров
- Создание через форму

Этап 8:
- Создание через HTMX форму + подгрузка списка
- Добавление через `hx-swap="beforeend"`
- Обработка out of band элементов
- Использование `hx-swap="none"`
- Возвращение нескольких кусков для замены: форма и oob-item
- https://htmx.org/attributes/hx-swap-oob/
- https://htmx.org/attributes/hx-swap/

Этап 9:
- Добавление CSRF (из Flask-WTF) защиты
- Обработка формы Flask-WTF для добавления товара
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/

Этап 10:
- Добавление заголовков `hx-headers`
- CSRF exempt
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#exclude-views-from-protection
- https://htmx.org/attributes/hx-headers/

Этап 11:
- Удаление товара
- Выбор цели:
  - по ближайшему тегу: `hx-target="closest li"`
  - по ближайшему классу: `hx-target="closest .product-item"`
- Анимации:
  - Загрузка `.htmx-request`
  - Замена `.htmx-swapping`
- https://htmx.org/attributes/hx-target/
- https://htmx.org/attributes/hx-indicator/
- https://htmx.org/attributes/hx-request/
- https://htmx.org/examples/animations/


Этап 12:
- Обновление товара:
  - PUT запрос
  - обработка ошибок (форма)

Этап 13:
- HTMX Push url - замена для истории браузера
- `hx-target="body"`
- `hx-confirm`
- https://htmx.org/attributes/hx-push-url/
- https://htmx.org/attributes/hx-confirm/

Этап 14:
- Автоматическая подгрузка в бесконечный список (с анимацией)
- `hx-trigger="revealed"`

Этап 15:
- Пагинация кнопками
