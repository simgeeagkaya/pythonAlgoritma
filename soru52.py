listem = []
durum = 0
toplam = 0
while durum < 10:
    sayı1 = int(input("Sayıyı giriniz: "))
    listem.append(sayı1)
    durum += 1

for i in listem:
    toplam += i

print (toplam)