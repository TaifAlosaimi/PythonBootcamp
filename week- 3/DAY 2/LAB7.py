rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total
print(f"{getTotal(199.99):.2f}")      #طريقة باستخدام f string تجعل بعد الفاصلة فقط رقمين
print(round(getTotal(199.99)))       #تقرب الرقم  لعدد عشري 
print(round(getTotal(199.99), 2))         #طريقة ثانية للرقمين بعد الفاصلة

