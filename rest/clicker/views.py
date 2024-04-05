from flask import Blueprint, render_template, request

from .crud import Clicker

clicker_app = Blueprint(
    "clicker_app",
    __name__,
)

app = clicker_app


clicker = Clicker()


@app.get("/", endpoint="index")
def show_clicker_page():
    return render_template(
        "clicker/index.html",
        count=clicker.count,
    )


@app.post("/", endpoint="do-click")
def handle_click():
    clicker.inc_count()
    return render_template(
        "clicker/index.html",
        count=clicker.count,
    )
