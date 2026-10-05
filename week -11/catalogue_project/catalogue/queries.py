from django.db.models import Avg, Count, Sum

from .models import Product


# Category Summary Report
category_report = (
    Product.objects
    .filter(is_active=True)
    .values("category_id", "category__name")
    .annotate(
        product_count=Count("id"),
        average_price=Avg("price"),
        total_stock=Sum("stock"),
    )
    .filter(product_count__gte=3)
    .order_by("-product_count", "category__name")
)


# Overall Product Summary
overall_summary = Product.objects.filter(
    is_active=True
).aggregate(
    total_products=Count("id"),
    average_price=Avg("price"),
)