from flask import Flask

from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app


def create_app():
    app = Flask(__name__)
    # if DEBUG:
    # app.config.update(
    #     TEMPLATES_AUTO_RELOAD=True,
    # )
    app.register_blueprint(index_app)
    app.register_blueprint(
        examples_app,
        url_prefix="/examples",
    )
    app.register_blueprint(
        clicker_app,
        url_prefix="/clicker",
    )
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
