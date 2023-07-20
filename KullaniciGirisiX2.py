print(""""***************

Kullanıcı girişi

*****************""")

sys_kullaniciadi="mehmet"
sys_parola="12345"
girisHakki=3

while True:
    kullaniciadi=input("Kullanıcı adi:")
    parola=input("Parola:")

    if(kullaniciadi!=sys_kullaniciadi and parola==sys_parola):
        print("Kullanıcı adı hatali...")
        girisHakki-=1
    elif(kullaniciadi==sys_kullaniciadi and parola!=sys_parola):
        print("Parola yanlış...")
        girisHakki-=1
    elif(kullaniciadi!=sys_kullaniciadi and parola!=sys_parola):
        print("Kullanıcı adı ve parola Hatali...")
        girisHakki-=1
    else:
        print("Sisteme başarı ile giriş yapıldı")
        break
    if(girisHakki==0):
        print("Giriş Hakkınız bitti")
        break