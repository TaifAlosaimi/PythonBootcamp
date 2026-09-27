from django.db import migrations


def fill_codes(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")

    for product in Product.objects.iterator():
        product.code = f"P{product.pk:06d}"
        product.save(update_fields=["code"])


def clear_codes(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")
    Product.objects.update(code=None)


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_add_product_code"),
    ]

    operations = [
        migrations.RunPython(fill_codes, clear_codes),
    ]