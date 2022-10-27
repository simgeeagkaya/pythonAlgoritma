x = int(input("işçi kaç saat çalışmıstır:"))
y = int(input("işçinin saatlik ücreti ne kadardır"))
kazanç = 0
if x >= 40:
   kazanç = ((x-40)*2*y)+(x*1*y)
   print("kazanç", kazanç)
elif x < 40:
    kazanç = (x*1*y)
    print("kazanç", kazanç)
