from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    NumberRange,
    ValidationError,
)

from .crud import products_storage


def validate_product_name(form, field):
    product_name = field.data
    if products_storage.name_exists(product_name):
        raise ValidationError(
            f"Product with {product_name!r} already exists!",
        )


class ProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        validators=[
            DataRequired(),
            validate_product_name,
        ],
    )
    price = IntegerField(
        label="Product price",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=99_999),
        ],
    )
    submit = SubmitField(label="Add product")
