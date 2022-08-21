#variables
bosluk = "-------------------------------------------"
bakiye = float(256037.75)
islem1 = int(1)
islem2 = int(2)

#interface
print(bosluk)
print("--------------------ATM--------------------")
print(bosluk)
kullanici_adi = input("Kullanıcı adını giriniz:")
print(bosluk)
print("Merhaba,", kullanici_adi, "bakiyeniz", bakiye, "tl")
print(bosluk)
print("------ Bakiye yatırmak için 1e basın ------")
print("------ Bakiye çekmek için 2ye basın  ------")
print(bosluk)

#işlemler
islem = int(input())
if islem == islem1:
 print(bosluk)
 print("-- Lütfen yatıracağınız miktarı giriniz --")
 print(bosluk)
 yatirilan = float(input())
 bakiye = bakiye + yatirilan
 print(bosluk)
 print("Yeni bakiyeniz ", bakiye, "tl dir.")
 print(bosluk)
elif islem == islem2:
 print(bosluk)
 print("----Lütfen çekeceğiniz miktari giriniz ----")
 print(bosluk)
 cekilen = float(input())
 if bakiye >= cekilen:
  bakiye = bakiye - cekilen
  print(bosluk)
  print("----------- İşleminiz başarılı ------------")
  print(bosluk)
  print("Kalan bakiyeniz: ", bakiye, "tl dir.")
 else: 
  print("----------- İşleminiz başarısız -----------")
else:
 print("----------- İşleminiz başarısız -----------")

#son