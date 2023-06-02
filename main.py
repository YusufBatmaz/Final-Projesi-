from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd


# Insan nesneleri
insan1 = Insan(12345678912, "Walter", "White", 50, "Erkek", "İngiliz")
insan2 = Insan(98765432148, "Kim", "Wexler", 35, "Kadın", "İngiliz")

# Issiz nesneleri
issiz1 = Issiz(12345678996, "Tommy", "Shelby", 40, "Erkek", "Fransız", 4, 4, 8)
issiz2 = Issiz(98765432147, "Salih", "Yatmaz", 30, "Erkek", "Türk", 6, 3, 0)
issiz3 = Issiz(45678912349, "Saul", "Kaya", 55, "Erkek", "Türk", 12, 4, 3)

# Calisan nesneleri
calisan1 = Calisan(12345678913, "Ali", "Yılmaz", 42, "Erkek", "Türk", "teknoloji", 24, 12000)
calisan2 = Calisan(96548712378, "Ayşe", "Demet", 35, "Kadın", "Türk", "muhasabe", 36, 18000)
calisan3 = Calisan(15935786286, "Mehmet", "Kaya",32, "Erkek", "Türk", "inşaat", 48, 22000)

# MaviYaka nesneleri
maviyaka1 = MaviYaka(12345678945, "Cüneyt", "Tepe", 42, "Erkek", "Türk", "teknoloji", 24, 12000, 0.2)
maviyaka2 = MaviYaka(96548712345, "Yusuf", "Varga", 35, "Erkek", "İspanyol", "muhasabe", 36, 18000, 0.5)
maviyaka3 = MaviYaka(15935786289, "Hirai", "Zer",32, "Erkek", "Türk", "inşaat", 48, 22000, 0.3)

# BeyazYaka nesneleri
beyazyaka1 = BeyazYaka(12345678978, "Tyler", "Durden", 42, "Erkek", "Alman", "teknoloji", 60, 12000, 3000)
beyazyaka2 = BeyazYaka(96548712345, "Skyler", "Black", 35, "Kadın", "İngiliz", "muhasabe", 12, 18000, 2500)
beyazyaka3 = BeyazYaka(15935786278, "Ahmet", "Korkmaz",32, "Erkek", "Türk", "inşaat", 48, 22000, 1000)

print("\n--- İnsan Sınıfının Nesne Bilgileri ---")
print(insan1)
print("\n**************************\n")
print(insan2)
print("\n**************************\n")

print("\n--- Issiz Sınıfının Nesne Bilgileri ---")
print(issiz1)
print("\n**************************\n")
print(issiz2)
print("\n**************************\n")
print(issiz3)
print("\n**************************\n")

print("\n--- Calisan Sınıfının Nesne Bilgileri ---")
print(calisan1)
print("\n**************************\n")
print(calisan2)
print("\n**************************\n")
print(calisan3)
print("\n**************************\n")

print("\n--- MaviYaka Sınıfının Nesne Bilgileri ---")
print(maviyaka1)
print("\n**************************\n")
print(maviyaka2)
print("\n**************************\n")
print(maviyaka3)
print("\n**************************\n")

print("\n--- BeyazYaka Sınıfının Nesne Bilgileri ---")
print(beyazyaka1)
print("\n**************************\n")
print(beyazyaka2)
print("\n**************************\n")
print(beyazyaka3)
print("\n**************************\n")

# DataFrame oluşturma
data = {
    "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan",
                     "Mavi Yaka", "Mavi Yaka", "Mavi Yaka",
                     "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],

    "TC No" : [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
               maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(),
               beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],

    "Ad" : [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
            maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(),
            beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],

    "Soyad" : [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
               maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(),
               beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],

    "Yaş" : [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
             maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(),
             beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],

    "Cinsiyet" : [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                  maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(),
                  beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],

    "Uyruk" : [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
               maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(),
               beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],

    "Sektör" : [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(),
               maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor(),
               beyazyaka1.get_sektor(), beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],

    "Tecrübe" : [int(calisan1.get_tecrube()/12), int(calisan2.get_tecrube()/12), int(calisan3.get_tecrube()/12),
                 int(maviyaka1.get_tecrube()/12), int(maviyaka2.get_tecrube()/12), int(maviyaka3.get_tecrube()/12),
                 int(beyazyaka1.get_tecrube()/12), int(beyazyaka2.get_tecrube()/12), int(beyazyaka3.get_tecrube()/12)],

    "Maaş" : [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(),
              maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(),
              beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],

    "Yıpranma Payı": [0, 0, 0, maviyaka1.get_yipranma_payi(),maviyaka2.get_yipranma_payi(),
                      maviyaka3.get_yipranma_payi(), 0, 0, 0],

    "Teşvik Primi": [0, 0, 0, 0, 0, 0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(),
                     beyazyaka3.get_tesvik_primi()],

    "Yeni Maaş": [int(calisan1.get_yeni_maas()), int(calisan2.get_yeni_maas()), int(calisan3.get_yeni_maas()),
                  int(maviyaka1.get_yeni_maas()), int(maviyaka2.get_yeni_maas()), int(maviyaka3.get_yeni_maas()),
                  int(beyazyaka1.get_yeni_maas()), int(beyazyaka2.get_yeni_maas()), int(beyazyaka3.get_yeni_maas())],

}

df = pd.DataFrame(data)

tecrube_ortalamasi = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}
yeni_maas_ortalamasi = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}
kisi_sayisi = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}

# b-)


# c-)
k15_uzeri_alan_sayisi = 0
try:
    for i in range(len(df)):
        if df.iloc[i, 9] > 15000:
            k15_uzeri_alan_sayisi += 1
    print(f"\n\nMaaşı 15000TL Üzeri Olan Kişi Sayısı = {k15_uzeri_alan_sayisi}")
except Exception as exception:
    print(f"HATA = {exception}")

# d-)
try:
    siralanmis_df = df.sort_values("Yeni Maaş", )
    print("\n\nDataframe'de Yeni Maaş Değerlerinin Küçükten Büyüğe Sıralanmış Hali\n")
    print(siralanmis_df.to_string())
except Exception as exception:
    print(f"HATA = {exception}")

# e-)
uc_sene_ustu_beyazyaka = []
try:
    for j in range(len(df)):
        if df.iloc[j, 8] > 3 and df.iloc[j, 0] == "Beyaz Yaka":
            uc_sene_ustu_beyazyaka.append(j)
    print("\n\nTecrübesi 3 Seneden Fazla Olan Beyaz Yakalılar")
    line = 1
    for i in uc_sene_ustu_beyazyaka:
        print(f"{line}. "
                f"{df.loc[i][2]} "
                f"{df.loc[i][3]}")
        line += 1
except Exception as exception:
    print(f"HATA = {exception}")


# f-)
print("\n\n2-5 Satır Aralığında Yeni Maaşı 10000TL Üzeri Olanlar")
try:
    for k in range(len(df)):
        if df.iloc[k, 12] > 10000 and 2 <= k <= 5:
            bilgiler = df.iloc[k, 1:13:11]
            print(f"Sıra Numarası = {k}\n"
                  f"{bilgiler.to_string()}\n")
except Exception as exception:
    print(f"HATA = {exception}")


# g-)
print("\n\nYeni DataFrame(Ad-Soyad-Sektör-Yeni Maaş Bilgilerini İçerir)")
try:
    dataframe_new = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]].copy()
    print(dataframe_new.to_string())
except Exception as exception:
    print(f"HATA = {exception}")







