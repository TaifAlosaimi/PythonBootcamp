def getVAT(total , rate = 0.15):
    """This function Will get the total with VAT added to it, and return the sum"""
    not_subtotal = total + (total* rate)
    return not_subtotal

print(getVAT(154))
print(getVAT(154, 0.05))
print(getVAT.__doc__)
help(getVAT)