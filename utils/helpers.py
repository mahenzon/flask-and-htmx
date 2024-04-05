from flask import request


def is_background_request():
    is_hx_request = request.headers.get("Hx-Request")

    return bool(is_hx_request)
