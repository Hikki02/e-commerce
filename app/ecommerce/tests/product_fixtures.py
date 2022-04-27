import pytest
from apps.products.models import Product


@pytest.fixture
def single_product(db, category_with_child):
    product = Product.objects.create(
        web_id="1",
        slug="product",
        name="product name 1",
        category=category_with_child,
        is_active=True
    )
    return product