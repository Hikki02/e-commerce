from django.urls import reverse

from apps.categories.models import Category


def test_create_category(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()
    print(new_category)
    print(get_category)
    assert new_category.id == get_category.id


def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = reverse('categories')
    response = api_client().get(endpoint)
    assert response.status_code == 200
    assert len(response.data) == len(category_with_multiple_children)


def test_create_category_with_child(category_with_child):
    new_sub_category = category_with_child
    get_category = Category.objects.all().first()
    assert get_category.children.first() == new_sub_category
