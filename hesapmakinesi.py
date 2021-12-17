print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""")
print("1=toplama,2=çıkarma,3=çarpma,4=bölme")

a=int(input("Birinci sayı="))
b=int(input("İkinci sayı="))

işlem=input("İşlem giriniz=")

if(işlem == "1"):
    print("{} ile {} toplamı {} dır".format(a,b,a+b))
elif(işlem == "2"):
    print("{} ile {} farkı {} dır".format(a,b,a-b))
elif(işlem == "3"):
    print("{} ile {} çarpımı {} dır".format(a,b,a*b))
elif(işlem == "4"):
    print("{} ile {} bölümü {} dır".format(a,b,a/b))
else:
    print("Eksik ya da hatalı tuşlama yaptınız.Lütfen kontrol ediniz.")