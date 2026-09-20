from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    sku = models.CharField(max_length=30, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def is_available(self):
        return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock

    def __str__(self):
        return f"{self.name} ({self.sku})"

    class Category(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        FOOD = "food", "Food"
        ACCESSORY = "accessory", "Accessory"

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY
    )

    description = models.TextField(blank=True)

    class Meta:
        ordering = ["category", "name"]

        verbose_name = "product"
        verbose_name_plural = "products"

        indexes = [
            models.Index(
                fields=["category", "is_active"],
                name="product_cat_active_idx",
            ),
        ]

        constraints = [
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name="product_price_nonneg",
            ),
            models.CheckConstraint(
                check=models.Q(stock__gte=0),
                name="product_stock_nonneg",
            ),
        ]