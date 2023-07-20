print("""*************
Finocci Sayısı Bulma
*************""")

a=1
b=1

sayi=int(input("fibonacci degerini girin"))

fibocci=[a,b]

for i in range(sayi+1):
    a,b=b,a+b

    fibocci.append(b)
print(fibocci)
