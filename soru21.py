istek = int(input('sinema icin 1,tiyatro için 2 yazınız'))
isStudent = int(input('öğrenciyseniz 1 değilseniz 2 yazınız'))
price = 0

if istek == 1:
    price = 49.5
else:
    price = 29.8


if isStudent == 1:
    print(price / 2, 'TL')
else:
    print(price, 'TL')

