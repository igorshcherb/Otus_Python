from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    """Класс для модели продуктов"""

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
    search_help_text = "Введите слово для поиска"

    actions = ("increment_price",)

    fields = ("name", "description", "price", "category")

    @admin.action(description="Увеличить цену продуктов на 10")
    def increment_price(self, request, queryset):
        """Увеличение цены продуктов на 10"""
        for product in queryset:
            product.price += 10
            product.save()
        self.message_user(
            request, message=f"Цена {queryset.count()} продуктов увеличена на 10"
        )
