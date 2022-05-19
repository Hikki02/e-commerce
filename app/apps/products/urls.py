from django.urls import path

from .views import ProductByCategory, ProductInventoryByWebId

urlpatterns = [
    path('product/<str:query>/', ProductByCategory.as_view(), name='product_detail'),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),

]
