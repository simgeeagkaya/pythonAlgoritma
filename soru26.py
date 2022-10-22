import random

rand_number = random.randint(0, 9)
count = 0
selected_number = 0

while selected_number != rand_number:
    selected_number = int(input("0-9 arasında bir sayı giriniz"))
    count += 1
    if selected_number == rand_number:
        print(count, ". denemede buldunuz tebrikler")
        break
    """" random 1-9 arasında sayı tanımladım while döngüsü ile sayıyı bulana kadar denettiriyorum
    sectiğim sayı ve random sayıyı bulunca break komutu ile durdurdum
    """