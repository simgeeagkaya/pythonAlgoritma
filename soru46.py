print("ikinci dereceden denklemin kökünü bulma")
# y = ax**2+bx+c
a = int(input("a değerini giriniz"))
b = int(input("b değerini giriniz"))
c = int(input("c değerini giriniz"))

delta = b**2-4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)
print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))
