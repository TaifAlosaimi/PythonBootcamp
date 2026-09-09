from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render


PRODUCTS = [
    {
        "id": 1,
        "name": "Classic Watch",
        "category": "Accessories",
        "price": 450,
        "rating": 4.8,
        "description": "A timeless watch with a clean and elegant design.",
    },
    {
        "id": 2,
        "name": "Leather Bag",
        "category": "Fashion",
        "price": 320,
        "rating": 4.5,
        "description": "A premium leather bag designed for everyday use.",
    },
    {
        "id": 3,
        "name": "Wireless Headphones",
        "category": "Electronics",
        "price": 650,
        "rating": 4.7,
        "description": "Comfortable wireless headphones with immersive sound.",
    },
    {
        "id": 4,
        "name": "Running Shoes",
        "category": "Sports",
        "price": 280,
        "rating": 4.3,
        "description": "Lightweight running shoes built for daily training.",
    },
    {
        "id": 5,
        "name": "Minimal Desk Lamp",
        "category": "Home",
        "price": 180,
        "rating": 4.6,
        "description": "A modern desk lamp with a minimal aesthetic.",
    },
    {
        "id": 6,
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 390,
        "rating": 4.9,
        "description": "A compact mechanical keyboard for a smooth typing experience.",
    },
]


def product_list(request):
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    sort = request.GET.get("sort", "").strip()

    filtered_products = PRODUCTS

    # Search by product name or description
    if q:
        filtered_products = [
            product
            for product in filtered_products
            if q.lower() in product["name"].lower()
            or q.lower() in product["description"].lower()
        ]

    # Filter by category
    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    # Filter by minimum price
    if min_price:
        try:
            min_price_value = float(min_price)

            filtered_products = [
                product
                for product in filtered_products
                if product["price"] >= min_price_value
            ]
        except ValueError:
            min_price = ""

    # Sort
    allowed_sort = {"price", "rating", "name"}


    if sort in allowed_sort:
        filtered_products = sorted(
            filtered_products,
            key=lambda product: product[sort]
        )





    # Pagination
    paginator = Paginator(filtered_products, 3)

    page_number = request.GET.get("page", "1")
    page_obj = paginator.get_page(page_number)

    # Preserve filters when moving between pages
    query_params = request.GET.copy()

    if "page" in query_params:
        query_params.pop("page")

    query_string = query_params.urlencode()

    categories = sorted(
        {product["category"] for product in PRODUCTS}
    )

    context = {
        "page_obj": page_obj,
        "q": q,
        "category": category,
        "min_price": min_price,
        "sort": sort,
        "categories": categories,
        "query_string": query_string,
    }

    return render(
        request,
        "products/product_list.html",
        context,
    )


def product_detail(request, id):
    product = next(
        (product for product in PRODUCTS if product["id"] == id),
        None,
    )

    if product is None:
        raise Http404("Product not found.")

    tab = request.GET.get("tab", "details").strip()

    allowed_tabs = {"details", "reviews", "shipping"}

    if tab not in allowed_tabs:
        tab = "details"

    context = {
        "product": product,
        "tab": tab,
    }

    return render(
        request,
        "products/product_detail.html",
        context,
    )