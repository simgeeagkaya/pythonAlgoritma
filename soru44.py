sayi = int(input("faktöriyelini bulmak istediğiniz sayıyı giriniz:"))
carpim = 1
for i in range(1, sayi):
     carpim *=(i+1)
     print(carpim)
