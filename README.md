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


## Главы (видео)

Ссылка на видео: 

### Этап 1:
[Ветка `checkpoint-01-init-app`](/mahenzon/flask-and-htmx/tree/checkpoint-01-init-app)
- Инициализация Flask приложения
- https://flask.palletsprojects.com/en/3.0.x/
- https://jinja.palletsprojects.com/en/3.1.x/templates/

### Этап 2:
[Ветка `checkpoint-02-install-htmx`](/mahenzon/flask-and-htmx/tree/checkpoint-02-install-htmx)
- Установка HTMX
- https://htmx.org/
- https://htmx.org/docs/

### Этап 3:
[Ветка `checkpoint-03-first-examples`](/mahenzon/flask-and-htmx/tree/checkpoint-03-first-examples)
- Ping
  - on click
  - on shift + click
- Hover
- HTMX:
  - `hx-swap="outerHTML"`
  - `hx-trigger="mouseenter"`
  - `hx-trigger="click[shiftKey]"`
- https://htmx.org/attributes/hx-trigger/

### Этап 4:
[Ветка `checkpoint-04-clicker`](/mahenzon/flask-and-htmx/tree/checkpoint-04-clicker)
- Clicker via HTMX
- https://htmx.org/attributes/hx-post/
- https://htmx.org/attributes/hx-swap/

### Этап 5:
[Ветка `checkpoint-05-embed-parts`](/mahenzon/flask-and-htmx/tree/checkpoint-05-embed-parts)
- Embed clicker into index via HTMX

### Этап 6:
[Ветка `checkpoint-06-htmx-boosts`](/mahenzon/flask-and-htmx/tree/checkpoint-06-htmx-boosts)
- Handle HTMX boosts
- https://htmx.org/attributes/hx-boost/

### Этап 7:
[Ветка `checkpoint-07-products-list`](/mahenzon/flask-and-htmx/tree/checkpoint-07-products-list)
- Список товаров
- Создание через форму

### Этап 8:
[Ветка `checkpoint-08-products-create-item`](/mahenzon/flask-and-htmx/tree/checkpoint-08-products-create-item)
- Создание через HTMX форму + подгрузка списка
- Добавление через `hx-swap="beforeend"`
- Обработка out of band элементов
- Использование `hx-swap="none"`
- Возвращение нескольких кусков для замены: форма и oob-item
- https://htmx.org/attributes/hx-swap-oob/
- https://htmx.org/attributes/hx-swap/

### Этап 9:
[Ветка `checkpoint-09-products-form-wtf`](/mahenzon/flask-and-htmx/tree/checkpoint-09-products-form-wtf)
- Добавление CSRF (из Flask-WTF) защиты
- Обработка формы Flask-WTF для добавления товара
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/

### Этап 10:
[Ветка `checkpoint-10-csrf-token-headers`](/mahenzon/flask-and-htmx/tree/checkpoint-10-csrf-token-headers)
- Добавление заголовков `hx-headers`
- CSRF exempt
- https://flask-wtf.readthedocs.io/en/1.2.x/csrf/#exclude-views-from-protection
- https://htmx.org/attributes/hx-headers/

### Этап 11:
[Ветка `checkpoint-11-product-delete-animation`](/mahenzon/flask-and-htmx/tree/checkpoint-11-product-delete-animation)
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


### Этап 12:
[Ветка `checkpoint-12-product-update`](/mahenzon/flask-and-htmx/tree/checkpoint-12-product-update)
- Обновление товара:
  - PUT запрос
  - обработка ошибок (форма)

### Этап 13:
[Ветка `checkpoint-13-product-details-delete`](/mahenzon/flask-and-htmx/tree/checkpoint-13-product-details-delete)
- HTMX Push url - замена для истории браузера
- `hx-target="body"`
- `hx-confirm`
- https://htmx.org/attributes/hx-push-url/
- https://htmx.org/attributes/hx-confirm/

### Этап 14:
[Ветка `checkpoint-14-products-pagination-reveal`](/mahenzon/flask-and-htmx/tree/checkpoint-14-products-pagination-reveal)
- Автоматическая подгрузка в бесконечный список (с анимацией)
- `hx-trigger="revealed"`

### Этап 15:
[Ветка `checkpoint-15-products-pagination-buttons`](/mahenzon/flask-and-htmx/tree/checkpoint-15-products-pagination-buttons)
- Пагинация кнопками
