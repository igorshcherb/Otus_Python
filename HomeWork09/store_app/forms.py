from django import forms

from .models import Product


class ProductModelForm(forms.ModelForm):
    """Класс для формирования формы для создания продукта"""

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
        labels = {
            "name": "Наименование продукта",
            "description": "Описание продукта",
            "price": "Цена продукта",
            "category": "Категория продукта",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите наименование продукта",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание продукта",
                },
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Введите цену продукта"}
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Выберите категорию продукта из списка",
                },
            ),
        }

    def clean_name(self):
        """Проверка длины наименования продукта"""
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError(
                "Наименование продукта должно быть более 3 символов"
            )
        return name

    def clean_price(self):
        """Проверка цены продукта"""
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Цена продукта должна быть больше 0")
        return price
