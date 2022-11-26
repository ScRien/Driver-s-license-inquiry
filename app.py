import datetime

def hesapla(dogumYili):
    if dogumYili == "" or dogumYili == None:
        print("Lütfen Geçerli bir değer giriniz!")
        sentence = input("Doğum Yılınız: ")
        hesapla(sentence)
    else:
        yil = datetime.datetime.now()
        yas = yil.year - int(dogumYili)
        if yas < 18:
            print(f"Yaşınız: {yas} olduğundan dolayı şuan ehliyet alamazsınız!")
        elif yas >= 18:
            print(f"Yaşınız: {yas} olduğundan dolayı şuan ehliyet alabilirsiniz!")

while True:
    sentence = input("Doğum Yılınız: ")
    hesapla(sentence)
