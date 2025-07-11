from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Category, Product
from .forms import ProductModelForm
from .tasks import ActionName, updated_product


class HomeTemplateView(TemplateView):
    template_name = "store_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        context["description"] = "Главная страница каталога"
        return context


class AboutTemplateView(TemplateView):
    template_name = "store_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас"
        context["description"] = "Информация о компании"
        return context


class ProductView:
    """Базовый класс для модели Product"""

    model = Product


class ProductListView(ProductView, ListView):
    """Представление для списка продуктов"""

    template_name = "store_app/product_list.html"
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(ProductView, DetailView):
    """Представление для деталей продукта"""

    template_name = "store_app/product_detail.html"
    context_object_name = "product"


class ProductCreateView(ProductView, CreateView):
    """Представление для отображения страницы создания продукта"""

    template_name = "store_app/product_create.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        # print(form)
        messages.success(self.request, "Продукт успешно создан")
        return super().form_valid(form)


class ProductUpdateView(ProductView, UpdateView):
    """Представление для редактирования продукта"""

    template_name = "store_app/product_edit.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно обновлен")
        return super().form_valid(form)


class ProductDeleteView(ProductView, DeleteView):
    """Представление для удаления продукта"""

    template_name = "store_app/product_delete.html"
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно удален")
        return super().form_valid(form)
