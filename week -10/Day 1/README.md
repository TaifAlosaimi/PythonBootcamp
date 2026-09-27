# Guided Lab — Evolve the Product Schema

This guided lab demonstrates how to safely evolve a Django database schema using schema migrations, data migrations, field renaming, migration dependencies, and rollback.

The main goal was to practice making database changes in a controlled and repeatable way while protecting existing data.

---

## Lab Objectives

- Add a new field to an existing model.
- Create and inspect schema migrations.
- Use `RunPython` for a data migration.
- Populate existing records with generated values.
- Make a field required and unique after existing data has been populated.
- Rename a field using `RenameField` without losing its data.
- Inspect migration dependencies.
- Test migration rollback and re-apply the migration.
- Verify the final database state.

---

## Project Structure

```text
week10_day1/
│
├── manage.py
├── README.md
│
├── catalog/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_add_product_code.py
│   │   ├── 0003_populate_product_code.py
│   │   ├── 0004_make_product_code_required_unique.py
│   │   └── 0005_rename_stock_to_quantity.py
│   │
│   ├── models.py
│   └── ...
│
└── week10_day1/
    ├── settings.py
    └── ...
```

---

# Migration Workflow

## Step 1 — Add `Product.code` with `null=True`

The first schema change added a new `code` field to the existing `Product` model.

The field was initially nullable so existing database rows could remain valid.

### Command

```bash
python manage.py makemigrations catalog
```

This created:

```text
0002_add_product_code.py
```

---

## Step 2 — Inspect Migration History

To inspect the migration files and their current state:

```bash
python manage.py showmigrations catalog
```

The migration list showed the migration history for the `catalog` app.

---

## Step 3 — Preview and Inspect the SQL

Before applying the migration, the planned operations were inspected with:

```bash
python manage.py migrate --plan
```

The SQL generated for migration `0002` was inspected with:

```bash
python manage.py sqlmigrate catalog 0002
```

This showed the SQL operation used to add the `code` column.

---

# Data Migration

## Step 4 — Create an Empty Data Migration

A separate empty migration was created for changing existing data:

```bash
python manage.py makemigrations catalog --empty --name populate_product_code
```

This created:

```text
0003_populate_product_code.py
```

The migration was used to populate the new `code` field for existing `Product` records.

The data migration used Django's `RunPython` operation.

---

## Step 5 — Populate Existing Product Codes

The migration generated a code from each Product primary key.

Conceptually:

```python
product.code = f"P{product.pk:06d}"
```

The data was then saved for the existing records.

This step is important because the database already contained products, and the new field needed valid values before it could safely become required.

---

# Enforcing Database Constraints

## Step 6 — Make `code` Required and Unique

After existing products had valid codes, the field was changed to:

```python
code = models.CharField(
    max_length=30,
    unique=True
)
```

The migration was created with:

```bash
python manage.py makemigrations catalog --name make_product_code_required_unique
```

Django created:

```text
0004_make_product_code_required_unique.py
```

Then the migration was applied:

```bash
python manage.py migrate
```

This demonstrates the safe sequence:

```text
Add nullable field
        ↓
Populate existing data
        ↓
Make field required + unique
```

---

# Renaming a Field Without Losing Data

## Step 7 — Rename `stock` to `quantity`

The existing field:

```text
stock
```

was renamed to:

```text
quantity
```

The migration was generated with:

```bash
python manage.py makemigrations catalog --name rename_stock_to_quantity
```

Django detected the field rename and asked whether:

```text
Was product.stock renamed to product.quantity?
```

The rename was confirmed.

This created:

```text
0005_rename_stock_to_quantity.py
```

The migration was then applied:

```bash
python manage.py migrate
```

The important point is that `RenameField` preserves the existing data, unlike removing the old field and creating a completely new one.

---

# Verifying the Data

The Django shell was opened with:

```bash
python manage.py shell
```

Then the Product model was imported:

```python
from catalog.models import Product
```

The records were inspected using:

```python
Product.objects.values()
```

This was used to verify that the Product data was still available after the field rename.

---

# Rollback Test

To test whether the migration history could safely move backwards, migration `0005` was rolled back:

```bash
python manage.py migrate catalog 0004
```

Django successfully unapplied:

```text
catalog.0005_rename_stock_to_quantity
```

This returned the database to the state represented by migration `0004`.

---

# Re-applying the Migration

After testing the rollback, the latest migration was applied again:

```bash
python manage.py migrate
```

The migration:

```text
0005_rename_stock_to_quantity
```

was successfully applied again.

---

# Final Migration Check

The final migration state was verified using:

```bash
python manage.py showmigrations catalog
```

The migration history showed all migrations as applied:

```text
[X] 0001_initial
[X] 0002_add_product_code
[X] 0003_populate_product_code
[X] 0004_make_product_code_required_unique
[X] 0005_rename_stock_to_quantity
```

---

# Migration Sequence

The complete schema evolution followed this sequence:

```text
0001
Initial Product model
        ↓
0002
Add code with null=True
        ↓
0003
Populate code for existing Products
        ↓
0004
Make code required and unique
        ↓
0005
Rename stock → quantity
        ↓
Rollback test
        ↓
Re-apply migration
```

---

# Why This Sequence Is Safe

A required field cannot simply be added to a table that already contains rows without providing valid values for those rows.

Therefore, the lab separated the schema and data changes:

1. Add the field as nullable.
2. Populate existing records.
3. Verify the data.
4. Enforce `required` and `unique` constraints.
5. Rename the existing field using `RenameField`.
6. Test rollback and re-apply the migration.

This makes database changes more predictable, reviewable, and reversible.

---

## Key Django Commands Used

| Command | Purpose |
|---|---|
| `python manage.py makemigrations catalog` | Create a migration from model changes |
| `python manage.py showmigrations catalog` | View migration history and status |
| `python manage.py migrate --plan` | Preview planned migrations |
| `python manage.py sqlmigrate catalog 0002` | Inspect SQL for a migration |
| `python manage.py makemigrations catalog --empty --name populate_product_code` | Create an empty data migration |
| `python manage.py migrate` | Apply migrations |
| `python manage.py shell` | Open the Django shell |
| `python manage.py migrate catalog 0004` | Roll back to migration `0004` |

---

## Key Concepts Practiced

- Schema migrations
- Data migrations
- `RunPython`
- `RenameField`
- Migration dependencies
- Nullable vs required fields
- Unique constraints
- Migration history
- Rollback
- Safe schema evolution
- Data preservation

---

## Conclusion

This lab demonstrated how Django migrations can be used to evolve an existing database safely.

The Product schema was changed incrementally, existing data was populated before constraints were enforced, the `stock` field was renamed without discarding its data, and the migration history was tested through rollback and re-application.
