import pytest

from apps.categories.models import Category


@pytest.fixture()
def single_category(db):
    return Category.objects.create(name="default", slug="default")


@pytest.fixture()
def category_with_child(db):
    parent = Category.objects.create(name='parent', slug='parent')
    parent.children.create(name='children', slug='children')
    child = parent.children.first()
    return child

