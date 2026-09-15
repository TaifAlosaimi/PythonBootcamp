# Create your views here.
from django.shortcuts import render, redirect


def home(request):
    # Read theme from Cookie
    theme = request.COOKIES.get("theme", "light")

    # Read cart from Session
    cart = request.session.get("cart", [])

    context = {
        "theme": theme,
        "cart": cart,
        "cart_count": len(cart),
    }

    return render(request, "preferences/home.html", context)


def set_theme(request, theme):
    # Allow only light or dark
    if theme not in ["light", "dark"]:
        return redirect("preferences:home")

    # Return the same page after setting the Cookie
    response = redirect("preferences:home")

    # Save theme for 30 days
    response.set_cookie(
        "theme",
        theme,
        max_age=60 * 60 * 24 * 30,
    )

    return response


def add_to_cart(request, product_id):
    # Get existing cart or create an empty one
    cart = request.session.get("cart", [])

    # Add product ID
    cart.append(product_id)

    # Save updated cart
    request.session["cart"] = cart

    return redirect("preferences:home")


def clear_cart(request):
    # Remove cart from Session
    request.session.pop("cart", None)

    return redirect("preferences:home")