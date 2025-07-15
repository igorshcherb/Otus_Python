from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import QueryGroup, Query

# from .forms import PostForm, PostModelForm


class HomeTemplateView(TemplateView):
    template_name = "dbbs_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "OTUS blog"
        context["description"] = "Добро пожаловать в OTUS blog"
        return context


class AboutTemplateView(TemplateView):
    template_name = "store_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас"
        context["description"] = "Информация о разработчике"
        return context


class QueryView:
    """Базовый класс для модели Product"""

    model = Query


class QueryListView(QueryView, ListView):
    """Представление для списка запросов"""

    template_name = "dbbs_app/query_list.html"
    context_object_name = "queries"
    paginate_by = 5


# def about(request):
#     return HttpResponse("<h1>About me info</h1>")
