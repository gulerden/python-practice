print("""ATM Makinesine Hoşgeldiniz
*******************

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ye basın

*******************""")

bakiye=1000
while True:
    islem=input("Yapacagınız işlemi seçiniz")
    if(islem=="q"):
        print("Yine Bekleriz")
        break
    if(islem=="1"):
        print("Bakiyeniz",bakiye)
    elif(islem=="2"):
        miktar=int(input("Yatıracagınız Miktarı Giriniz"))
        bakiye+=miktar
    elif(islem=="3"):
        miktar=int(input("Çekeceginiz para miktarını giriniz"))
        if(bakiye<miktar):
            print("Hesabinizda Yeterli para bulunmamaktadır")
            continue
        bakiye-=miktar
