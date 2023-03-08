def asalmi (sayi):
    if  sayi == 1:
        print("1 asal sayı değildir.")
        return
    elif sayi == 2:
        print("2 en küçük asal sayıdır.")
        return
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                print("Asal değildir.")
                return
            else:
                print("Sayı Asaldır.")
                return


asalmi(23)
