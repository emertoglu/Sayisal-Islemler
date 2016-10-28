def asal(kaca_kadar):
    """Asal sayý bulan fonksiyon
    Girdi olarak bir sayý alýr
    Bu sayýya kadar olan asal sayýlarý ekrana basar.
    """
    if kaca_kadar < 2:
        return
    elif kaca_kadar == 2:
        print(2)
        return
    else:
        print(2)
        for i in range(3,kaca_kadar):
            bolundu = False
            for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    break
            if bolundu == False:
                print(i)

x=eval(input("bir sayi giriniz:"))

asal(x)
