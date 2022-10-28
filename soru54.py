liste = []
adet = int(input('Kaç Sayı Girilecek: '))
for n in range(adet):
    sayi = int(input('Sayıyı Gir: '))
    liste.append(sayi)

en_kucuk = min(liste)
en_buyuk = max(liste)

print("Liste İçindeki En Büyük Sayı :", en_buyuk, "\nListe İçindeki En KÜÇÜK Sayı :", en_kucuk)

