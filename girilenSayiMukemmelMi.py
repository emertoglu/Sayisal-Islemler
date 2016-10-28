x=eval(input("sayi gir:"))
toplam=0

for i in range(1,x):
    if(x%i==0):
        toplam=toplam+i
if(x==toplam):
    print ("mukemmel")
else:
    print ("mukemmel degil")
