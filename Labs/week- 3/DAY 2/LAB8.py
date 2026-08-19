def inspect_order(item, qty):             #سويت داله وحطيت لها بارميترز
    subtotal = 25 * qty
    print(locals())               #locals() is a dictionary for locals variables فا بتطبع لي كل اللوكلز
    print(locals()["subtotal"])             #رح يطبع الsubtotal من اللوكلز
inspect_order("Pen", 10)