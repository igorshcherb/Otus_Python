from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path(
        "product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("product_create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product_edit/<int:pk>/", views.ProductUpdateView.as_view(), name="product_edit"
    ),
    path(
        "product_delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
