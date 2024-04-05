from flask import request


def is_background_request():
    is_hx_request = request.headers.get("Hx-Request")
    is_hx_boosted = request.headers.get("Hx-Boosted")

    return bool(is_hx_request and not is_hx_boosted)
