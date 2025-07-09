from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    """Класс для хранения модели продуктов для админ панели"""

    list_display = (
        "id",
        "name",
        "price",
        "category",
        "created_at",
    )
    ordering = ("id",)
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
    search_help_text = "Введите слово для поиска названии категории, либо в описании"

    actions = (
        "increment_price",
        "decrement_price",
    )

    @admin.action(description="Увеличить цену продуктов на 10")
    def increment_price(self, request, queryset):
        """Метод для action действия для увеличения цены продуктов на 10"""
        for product in queryset:
            product.price += 10
            product.save()
        self.message_user(
            request, message=f"Цена {queryset.count()} продуктов увеличена на 10"
        )

    @admin.action(description="Уменьшить цену продуктов на 10")
    def decrement_price(self, request, queryset):
        """Метод для action действия для уменьшения цены продуктов на 10"""
        for product in queryset:
            product.price -= 10
            product.save()
        self.message_user(
            request, message=f"Цена {queryset.count()} продуктов уменьшена на 10"
        )
