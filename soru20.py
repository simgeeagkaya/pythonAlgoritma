sayi1 = int(input('birinci sayıyı girin'))
sayi2 = int(input('ikinci sayıyı girin'))
toplam = 0
for sayac in range(sayi1, sayi2, 1):
    toplam = sayac + toplam
print(toplam)
