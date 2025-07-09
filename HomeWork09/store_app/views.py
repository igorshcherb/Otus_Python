from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Category, Product
from .forms import ProductModelForm
from .tasks import ActionName, updated_product


def home(request):
    """Представление для главной страницы"""
    return render(request, template_name="store_app/home.html")


def about(request):
    """Представление для страницы about"""
    return render(request, "store_app/about.html")


class ProductView:
    """Базовый класс для модели Product"""

    model = Product


class ProductListView(ProductView, ListView):
    """Представление для списка продуктов"""

    template_name = "store_app/product_list.html"
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(ProductView, DetailView):
    """Представление для отображения деталей продукта"""

    template_name = "store_app/product_detail.html"
    context_object_name = "product"


class ProductCreateView(ProductView, CreateView):
    """Представление для отображения страницы создания продукта"""

    template_name = "store_app/product_create.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        updated_product.delay(
            action_name=ActionName.created, product_name=form.instance.name
        )
        messages.success(
            self.request, f'Продукт "{form.instance.name}" успешно создан!'
        )
        return response


class ProductUpdateView(ProductView, UpdateView):
    """Представление для редактирования продукта"""

    template_name = "store_app/product_edit.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        updated_product.delay(
            action_name=ActionName.updated, product_name=form.instance.name
        )
        messages.success(
            self.request, f'Продукт "{form.instance.name}" успешно изменен!'
        )
        return response
