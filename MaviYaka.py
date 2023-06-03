from Calisan import Calisan


class MaviYaka(Calisan):
    # Değişkenlere göre Initializer metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    #  Gerekli değişkenler için get/set metotları
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    # Çalışanın zam hakkını hesaplayan zam_hakki metodu
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                zam_oran = 0
            elif 2 <= self.get_tecrube() < 4 and self.get_maas() < 15000:
                zam_oran = (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10)
            elif self.get_tecrube() >= 4 and self.get_maas() < 25000:
                zam_oran = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
            else:
                zam_oran = self.get_maas()

            self.set_yeni_maas(self.get_maas() + ((self.get_maas() / 100) * zam_oran))

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
