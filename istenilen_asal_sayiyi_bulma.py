liste=[2]
sayac=0
i=2
x=eval(input("kacinci sayi hesaplansin:"))
while(i>0):
    i=i+1
    asal=True
    for j in range(2,i):
        if(i%j==0):
            asal=False
            break
    if(asal==True ):
        liste.append(i)       
    if(len(liste)==x):
        #print liste
        print (x,". asal sayi= ", liste[x-1])
        break


    
