from flask import Flask

from csrf_protection import csrf
from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app
from rest.products import products_app


def create_app():
    app = Flask(__name__)
    # if DEBUG:
    app.config.update(
        # TEMPLATES_AUTO_RELOAD=True,
        # python -c 'import secrets; print(secrets.token_hex())'
        SECRET_KEY="7b0969733518414e45c36a1618f11671412b033219edcc812494bfeca979ae17",
    )
    csrf.init_app(app)

    app.register_blueprint(index_app)
    app.register_blueprint(
        examples_app,
        url_prefix="/examples",
    )
    app.register_blueprint(
        clicker_app,
        url_prefix="/clicker",
    )
    app.register_blueprint(
        products_app,
        url_prefix="/products",
    )
    return app


def main():
    app = create_app()
    app.run(debug=True, port=5050)


if __name__ == "__main__":
    main()
