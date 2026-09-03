**URL collision**

urlpatterns = [
    path("products/create/", create_view),
    path("products/<str:id>/", details_view),
]


# 1. What happens when I access /products/create/?
## Answer:
Django calls create_view.

## Justification:
Django checks URL patterns from top to bottom.
The first pattern matches /products/create/, so Django stops there and calls create_view.

Although <str:id> could also match "create", Django does not continue after finding the first match.
So .. First match wins.




# 2. How do I view product ID = "create"?
## Answer :
I cannot access the product with ID "create" using /products/create/ with these URL patterns.

## Justification:
There is a URL collision between the fixed route:
    path("products/create/", create_view)
and the dynamic route:
    path("products/<str:id>/", details_view)

The dynamic route could interpret "create" as the product ID, but Django always matches the first route first.

Therefore, the URL structure must be changed to avoid the collision.
