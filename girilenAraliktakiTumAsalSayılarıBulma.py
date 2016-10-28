liste=[]
#liste2=[]

x=eval(input("alt tabani girin:"))
y=eval(input("ust tabani girin:"))

for i in range(x,y+1):
    asal=True
    for j in range(2,i):
        if(i%j==0):
            asal=False
            break
    if(asal==True):
        liste.append(i)
        
print(liste)

