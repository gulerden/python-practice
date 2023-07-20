print("""******************

Faktöriyel Bulma

Çıkmak için 'q' ye basın
******************""")

while True:
    sayi=input("sayi")
    if(sayi=="q"):
        print("Çıkış yapıldı")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1

        for i in range(2,sayi+1):
            faktoriyel*=i
        print("faktöriyel",faktoriyel)
