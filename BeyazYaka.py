from Calisan import Calisan


class BeyazYaka(Calisan):
    # Değişkenlere göre Initializer metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # Gerekli değişkenler için get/set metotları
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # Çalışanın zam hakkını hesaplayan zam_hakki metodu
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                zam = 0
            elif 2 <= self.get_tecrube() < 4 and self.get_maas() < 15000:
                zam = ((self.get_maas() % self.get_tecrube()) * 5) + self.__tesvik_primi
            elif self.get_tecrube() >= 4 and self.get_maas() < 25000:
                zam = ((self.get_maas() % self.get_tecrube()) * 4) + self.__tesvik_primi
            else:
                zam = 0

            self.set_yeni_maas(self.get_maas() + zam)
            # Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanır
            if self.get_yeni_maas() == self.get_maas():
                self.set_yeni_maas(self.get_maas())

        except Exception as e:
            print("Hata:", str(e))

    # ad, soyad, tecrübe ve yeni maaşı bilgilerini yazdıran method
    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay" \
               f"\nYeni Maaş: {self.get_yeni_maas()}"
