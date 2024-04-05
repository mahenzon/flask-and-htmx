from http import HTTPStatus

from flask import (
    Blueprint,
    request,
    render_template,
    Response,
)
from werkzeug.exceptions import HTTPException

from .crud import products_storage
from .forms import ProductForm

products_app = Blueprint(
    "products_app",
    __name__,
)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    form = ProductForm()
    products = products_storage.get_list()
    return render_template(
        "products/list.html",
        products=products,
        form=form,
    )


@app.post("/", endpoint="create")
def create_product():
    form = ProductForm()
    if not form.validate_on_submit():
        response = Response(
            render_template(
                "products/components/form.html",
                form=form,
            ),
            status=HTTPStatus.UNPROCESSABLE_ENTITY,
        )
        raise HTTPException(response=response)

    product = products_storage.add(
        product_name=form.name.data,
        product_price=form.price.data,
    )
    return render_template(
        "products/components/form-and-item-oob.html",
        product=product,
        form=ProductForm(formdata=None),
    )


@app.delete("/<int:product_id>/", endpoint="delete")
def delete_product(product_id: int):
    products_storage.delete(product_id)
    return Response(status=HTTPStatus.NO_CONTENT)
