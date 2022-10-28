poz = []
neg = []
i = 0

while i < 10:
    sayi1 = int(input("Sayı giriniz: "))
    i += 1

    if sayi1 < 0:
        neg.append(sayi1)

    elif sayi1 > 0:
        poz.append(sayi1)

lengpoz = len(poz)
lengneg = len(neg)

print("Pozitif sayı adedi : ", lengpoz)
print("Negatif sayı adedi : ", lengneg)
