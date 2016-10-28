fib=[1,1]

x=eval(input("kacinci fib sayisi  hesaplansin:"))

for i in range(2,x):
    fib.append(fib[i-2]+fib[i-1])
print (fib[i])

