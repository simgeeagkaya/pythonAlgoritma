yemek = input("yemek ismini giriniz: ")
menu = {
"tavuk doner": 15,
"hatay durum": 15,
"tam ekmek tavuk doner ": 19,
"pizza": 20,
"iskender": 25,
"köfte ekmek": 30,
"tavuk pilav": 65,
"serpme kahvaltı ": 120,
"pide": 20,
}

if yemek in menu:
    print(menu[yemek])
else:
    print("kelime  bulunamadı")