import datetime

i = int(input("Doğum Yılınızı Girin(YYYY) :"))
guncel_tarih = datetime.datetime.now()
# bugünün tam tarihi
guncel_yil = guncel_tarih.year
# bugünün yılı
yas = (guncel_yil - i)
print("yaşınız {}'dır".format(yas))
