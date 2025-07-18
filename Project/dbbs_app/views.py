from django.shortcuts import render, redirect
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
from .models import (
    Query,
    QueryGroup,
    QueryInGroup,
    Benchmark,
    BenchmarkItem,
    CompareBenchmarkItem,
)

from .forms import (
    QueryModelForm,
    QueryGroupModelForm,
    QueryInGroupModelForm,
    CompareParamsForm,
)


class HomeTemplateView(TemplateView):
    """Представление для начальной страницы"""

    template_name = "dbbs_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "DBBS"
        context["description"] = (
            "Система анализа производительности СУБД и MPP-кластеров DBBS - DataBase Benchmark System"
        )
        return context


class AboutTemplateView(TemplateView):
    """Представление для страницы 'О нас'"""

    template_name = "dbbs_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас"
        context["description"] = "Информация о разработчике"
        return context


class QueryView:
    """Базовый класс для модели Query"""

    model = Query


class QueryListView(QueryView, ListView):
    """Представление для списка запросов"""

    template_name = "dbbs_app/query_list.html"
    context_object_name = "queries"
    paginate_by = 3


class QueryDetailView(QueryView, DetailView):
    """Представление для деталей запроса"""

    template_name = "dbbs_app/query_detail.html"
    context_object_name = "query"


class QueryUpdateView(QueryView, UpdateView):
    """Представление для редактирования запроса"""

    template_name = "dbbs_app/query_edit.html"
    form_class = QueryModelForm
    success_url = reverse_lazy("query_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос успешно обновлен")
        return super().form_valid(form)


class QueryDeleteView(QueryView, DeleteView):
    """Представление для удаления запроса"""

    template_name = "dbbs_app/query_delete.html"
    success_url = reverse_lazy("query_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос успешно удален")
        return super().form_valid(form)


class QueryCreateView(QueryView, CreateView):
    """Представление для создания запроса"""

    template_name = "dbbs_app/query_create.html"
    form_class = QueryModelForm
    success_url = reverse_lazy("query_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос успешно создан")
        return super().form_valid(form)


class QueryGroupView:
    """Базовый класс для модели QueryGroup"""

    model = QueryGroup


class QueryGroupListView(QueryGroupView, ListView):
    """Представление для списка групп запросов"""

    template_name = "dbbs_app/query_group_list.html"
    context_object_name = "query_groups"
    paginate_by = 3


class QueryGroupDetailView(QueryGroupView, DetailView):
    """Представление для деталей группы запроса"""

    template_name = "dbbs_app/query_group_detail.html"
    context_object_name = "query_group"


class QueryGroupUpdateView(QueryGroupView, UpdateView):
    """Представление для редактирования группы запроса"""

    template_name = "dbbs_app/query_group_edit.html"
    form_class = QueryGroupModelForm
    success_url = reverse_lazy("query_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Группа запросов успешно обновлена")
        return super().form_valid(form)


class QueryGroupDeleteView(QueryGroupView, DeleteView):
    """Представление для удаления группы запроса"""

    template_name = "dbbs_app/query_group_delete.html"
    success_url = reverse_lazy("query_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Группа запросов успешно удалена")
        return super().form_valid(form)


class QueryGroupCreateView(QueryGroupView, CreateView):
    """Представление для создания группы запроса"""

    template_name = "dbbs_app/query_group_create.html"
    form_class = QueryGroupModelForm
    success_url = reverse_lazy("query_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Группа запросов успешно создана")
        return super().form_valid(form)


class QueryInGroupView:
    """Базовый класс для модели QueryInGroup"""

    model = QueryInGroup


class QueryInGroupListView(QueryInGroupView, ListView):
    """Представление для списка запросов в группах"""

    template_name = "dbbs_app/query_in_group_list.html"
    context_object_name = "queries_in_groups"
    paginate_by = 3


class QueryInGroupDetailView(QueryInGroupView, DetailView):
    """Представление для деталей запроса в группе"""

    template_name = "dbbs_app/query_in_group_detail.html"
    context_object_name = "query_in_group"


class QueryInGroupUpdateView(QueryInGroupView, UpdateView):
    """Представление для редактирования запроса в группе"""

    template_name = "dbbs_app/query_in_group_edit.html"
    form_class = QueryInGroupModelForm
    success_url = reverse_lazy("query_in_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос в группе успешно обновлен")
        return super().form_valid(form)


class QueryInGroupDeleteView(QueryInGroupView, DeleteView):
    """Представление для удаления запроса из группы"""

    template_name = "dbbs_app/query_in_group_delete.html"
    success_url = reverse_lazy("query_in_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос успешно удален из группы")
        return super().form_valid(form)


class QueryInGroupCreateView(QueryInGroupView, CreateView):
    """Представление для создания запроса в группе"""

    template_name = "dbbs_app/query_in_group_create.html"
    form_class = QueryInGroupModelForm
    success_url = reverse_lazy("query_in_group_list")

    def form_valid(self, form):
        messages.success(self.request, "Запрос успешно добавлен в группу")
        return super().form_valid(form)


class BenchmarkListView(ListView):
    """Представление для списка тестов производительности"""

    model = Benchmark
    template_name = "dbbs_app/benchmark_list.html"
    context_object_name = "benchmarks"
    paginate_by = 3


class BenchmarkItemListView(ListView):
    """Представление для списка элементов тестов производительности"""

    model = BenchmarkItem
    template_name = "dbbs_app/benchmark_item_list.html"
    context_object_name = "benchmark_items"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        benchmark = self.kwargs.get("benchmark")
        if benchmark:
            queryset = queryset.filter(benchmark=benchmark)
        return queryset


class CompareBenchmarkListView(ListView):
    """Представление для списка сравнения тестов производительности"""

    model = CompareBenchmarkItem
    template_name = "dbbs_app/compare_benchmark_list.html"
    context_object_name = "compare_benchmarks"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        benchmark_name_1 = self.kwargs.get("benchmark_name_1")
        benchmark_name_2 = self.kwargs.get("benchmark_name_2")
        if benchmark_name_1 and benchmark_name_2:
            queryset = queryset.filter(
                benchmark_name_1=benchmark_name_1, benchmark_name_2=benchmark_name_2
            )
        return queryset


def compare_params_view(request):
    if request.method == "POST":
        form = CompareParamsForm(request.POST)
        if form.is_valid():
            benchmark_name_1 = form.cleaned_data["benchmark_name_1"]
            benchmark_name_2 = form.cleaned_data["benchmark_name_2"]
            return redirect(
                f"/compare_benchmarks/{benchmark_name_1}/{benchmark_name_2}"
            )
    else:
        form = CompareParamsForm()
    return render(request, "dbbs_app/compare_params.html", {"form": form})
