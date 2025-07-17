from django import forms
from django.core.exceptions import ValidationError

from .models import Query, QueryGroup, QueryInGroup


class QueryModelForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ["code", "query_text", "description"]
        labels = {
            "code": "Код",
            "query_text": "Текст",
            "description": "Описание",
        }
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите код"}
            ),
            "query_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите текст запроса",
                }
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите описание"}
            ),
        }


class QueryGroupModelForm(forms.ModelForm):
    class Meta:
        model = QueryGroup
        fields = ["code", "description"]
        labels = {
            "code": "Код",
            "description": "Описание",
        }
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите код"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите описание"}
            ),
        }


class QueryInGroupModelForm(forms.ModelForm):
    class Meta:
        model = QueryInGroup
        fields = ["query_group", "query"]
        labels = {
            "query_group": "Группа запросов",
            "query": "Запрос",
        }
        widgets = {
            "query_group": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите группу запросов",
                }
            ),
            "query": forms.Select(
                attrs={"class": "form-control", "placeholder": "Введите запрос"}
            ),
        }
