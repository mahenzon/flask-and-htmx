from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    @property
    def names(self) -> set[str]:
        return {product.name for product in self.products.values()}

    def add(self, product_name: str, product_price: int) -> Product:
        product = Product(
            id=self.next_id,
            name=product_name,
            price=product_price,
        )
        self.products[product.id] = product
        return product

    def get_list(self) -> list[Product]:
        return list(self.products.values())

    def name_exists(self, product_name: str) -> bool:
        return product_name in self.names


products_storage = ProductsStorage()

products_storage.add(
    "Laptop",
    1299,
)
products_storage.add(
    "Desktop",
    1999,
)
products_storage.add(
    "Smartphone",
    1099,
)
