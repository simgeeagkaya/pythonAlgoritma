deger = int(input('sayı giriniz'))
cift = 0
tek = 0

for sayac in range(1, deger):
    if sayac % 2:
        tek = tek + sayac
    else:
        cift = cift + sayac

print('tek sayıların toplamı: ', tek, 'cift sayıların toplamı: ', cift)
## toplam olarak gidilecegi icin tek ve çiftleri 0 dan baslattım for ile aralıgını belirliyorum
# tek ve cifleri belirleyip her bulduğum değere topluyorum