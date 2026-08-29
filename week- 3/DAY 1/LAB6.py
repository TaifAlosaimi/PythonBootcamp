def getVAT(total , rate = 0.15):
    """This function Will get the total with VAT added to it, and return the sum"""     #Docstring فقط شرح للدالة
    not_subtotal = total + (total* rate)
    return not_subtotal

print(getVAT(154))                          #اعطيت الدالة توتل واستدعيت الrate ألموجود , ماغيرته
print(getVAT(154, 0.05))               #غيرت قيمة ال rate
print(getVAT.__doc__)                  #ابغى اطبع الدكمنتيشن 
help(getVAT)                    #رح يعطيني معلومات عن الفنكشن