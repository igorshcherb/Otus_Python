from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path(
        "product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("product_create/", views.add_product, name="product_create"),
    path("product_edit/<int:product_id>/", views.product_edit, name="product_edit"),
]
