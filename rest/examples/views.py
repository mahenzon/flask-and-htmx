from flask import (
    Blueprint,
    render_template,
    request,
)

from csrf_protection import csrf


examples_app = Blueprint(
    "examples_app",
    __name__,
)

app = examples_app


@app.get("/", endpoint="index")
def examples_list():
    return render_template("examples/index.html")


@app.route(
    "/ping/",
    methods=["GET", "POST"],
    endpoint="ping",
)
def handle_ping():
    if request.method == "POST":
        return "Pong!"
    return render_template("examples/ping/show-ping.html")


@app.route(
    "/hover/",
    methods=["GET", "POST"],
    endpoint="hover",
)
@csrf.exempt
def handle_hover():
    if request.method == "POST":
        return "I see you! (only once)"
    return render_template("examples/hover/show-hover.html")
