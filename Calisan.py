from Insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.kontrol_sektor(sektor)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = ""

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.kontrol_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    def zam_hakki(self):
        try:
            if self.__tecrube / 12 < 2:
                zam_oran = 0
            elif 2 <= self.__tecrube / 12 < 4 and self.__maas < 15000:
                zam_oran = self.__maas % self.__tecrube
            elif self.__tecrube / 12 >= 4 and self.__maas < 25000:
                zam_oran = (self.__maas % self.__tecrube) / 2
            else:
                zam_oran = 0

            self.__yeni_maas = self.__maas + ((self.__maas / 100) * zam_oran)

            if self.__yeni_maas == self.__maas:
                self.__yeni_maas = self.__maas
        except Exception as e:
            print("Hata:", str(e))

    def kontrol_sektor(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in sektorler:
            return sektor
        else:
            return "diğer"

    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {self.__yeni_maas}"