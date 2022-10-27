alış = int(input("ürünün alış fiyatını yazınız:"))
kdv = 18/100
alısk = alış-(alış*kdv)
kar = int(input("karı nedir: "))
satış = alısk + kar
print("satış:", satış)
