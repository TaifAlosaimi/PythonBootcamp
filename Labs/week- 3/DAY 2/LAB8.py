def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])
inspect_order("Pen", 10)