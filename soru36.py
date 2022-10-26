import datetime

gun = int(input("Doğum Gününüzün Gününü Giriniz:"))
ay = int(input("Doğum Gününüzün ayınızı Giriniz:"))
yil = int(input("Doğum Gününüzün Yılınızı Giriniz:"))


for x in range(yil,datetime.datetime.now().year+1):

    dogumtarihi = datetime.datetime(x,ay,gun).strftime("%A")
    print(dogumtarihi)



