menu = {
"tavuk doner": 15,
"hatay durum": 15,
"tavuk doner ": 19,
"pizza": 20,
"iskender": 25,
"köfte ekmek": 30,
"tavuk pilav": 65,
"serpme kahvaltı ": 120,
"pide": 20,
}
hesap = 0

while True :
 yemek =input("ne yemek yer ")
 if yemek == "$":
   break

 hesap+=menu[yemek]

print("Hesabınız:",hesap)







