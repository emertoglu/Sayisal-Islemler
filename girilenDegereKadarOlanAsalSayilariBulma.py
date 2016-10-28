y=3
z=1
asal=True
x=eval(input("bir sayi giriniz:"))
while y<=x:
    asal = True
    z = 3
    while z<y:

        kalan=y%z
        if kalan==0:
            asal = False
            break
        z=z+1
    if asal:
        print (y, "sayisi bir asal sayidir")
    y=y+1


