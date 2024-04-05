from flask import Blueprint, render_template, request

from utils.helpers import is_background_request
from .crud import Clicker

clicker_app = Blueprint(
    "clicker_app",
    __name__,
)

app = clicker_app


clicker = Clicker()


@app.get("/", endpoint="index")
def show_clicker_page():
    template_name = "clicker/index.html"
    if is_background_request():
        template_name = "clicker/components/clicker-body.html"
    return render_template(
        template_name,
        count=clicker.count,
    )


@app.post("/", endpoint="do-click")
def handle_click():
    clicker.inc_count()
    template_name = "clicker/index.html"
    if is_background_request():
        template_name = "clicker/components/click-count.html"
    return render_template(
        template_name,
        count=clicker.count,
    )
