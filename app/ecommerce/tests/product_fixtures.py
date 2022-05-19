import pytest
from apps.products.models import Product, Media, ProductType, ProductAttribute, Brand, ProductAttributeValue, \
    ProductInventory


@pytest.fixture
def product_type(db, product_attribute):
    product_type = ProductType.objects.create(name='default')
    product_attribute = product_attribute
    product_type.product_type_attribute.add(product_attribute)
    return product_type


@pytest.fixture
def product_attribute(db):
    product_attribute = ProductAttribute.objects.create(
        name="default", description="default",
    )
    return product_attribute


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


@pytest.fixture
def brand(db):
    brand = Brand.objects.create(
        name="default"
    )
    return brand


@pytest.fixture
def product_attribute_value(db, product_attribute):
    product_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=product_attribute,
        attribute_value="default",
    )
    return product_attribute_value


@pytest.fixture
def single_sub_product_with_media_and_attributes(db, single_product, product_type, brand, product_attribute_value):
    sub_product = ProductInventory.objects.create(
        sku="123456789",
        upc="100000000001",
        product_type=product_type,
        product=single_product,
        brand=brand,
        is_active=True,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        sale_price="9.99",
        is_on_sale=False,
        is_digital=False,
        weight=1000.0,
    )

    media = Media.objects.create(
        product_inventory=sub_product,
        img_url="images/default.png",
        alt_text="default",
        is_feature=True,
    )

    product_attribute_value = product_attribute_value
    sub_product.attribute_values.add(product_attribute_value)

    return {
        "inventory": sub_product,
        "media": media,
        "attribute": product_attribute_value,
    }

