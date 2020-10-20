import random
import time

print("""***************************

Sayı Tahmin Oyunu

1 ile 40 arasındaki sayıyı tahmin edin

**************************""")

rastgele_sayı = random.randint(1,40)

tahmin_hakkı = 7

while True :

     tahmin =(int(input("Tahmininiz:")))
     if (tahmin < rastgele_sayı):
         print("Bilgiler Sorgulanıyor...")
         time.sleep(1)
         print("Tahmininiz, bulmanız gereken rakamdan daha küçük, bir daha deneyin")
         tahmin_hakkı -= 1
         print("Kalan tahmin hakkınız:",tahmin_hakkı)
     elif(tahmin < rastgele_sayı):
         print("Bilgiler Sorgulanıyor...")
         time.sleep(1)
         print("Tahmininiz, bulmanız gereken rakamdan daha büyük, bir daha deneyin")
         tahmin_hakkı -= 1
         print("Kalan tahmin hakkınız:",tahmin_hakkı)
     else:
         print("Bilgiler sorgulanıyor...")
         time.sleep(1)
         print("Tebrikler tahmininiz doğru")
         print("Kalan hakkınız şu kadardı:",tahmin_hakkı)
         break
     if (tahmin_hakkı==0):
         print("Tahmin hakkınız bitti, malesef doğru sayıyı bulamadınız")
         print("Doğru sayımız :",rastgele_sayı)
         break



