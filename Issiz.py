from Insan import Insan


class Issiz(Insan):
    # Değişkene göre Initializer metot veriliyor
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, mavi_statu, beyaz_statu, yonetici_statu):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = {"mavi yaka": mavi_statu, "beyaz yaka": beyaz_statu, "yönetici": yonetici_statu}
        self.__statu = ""

    # Değişkenler için get/set metotları verilen kısım
    def get_tecrube_dict(self):
        return self.__tecrube_dict

    def set_tecrube_dict(self, statu, yil):
        self.__tecrube_dict[statu] = yil

    def get_statu(self):
        return self.__statu

    def set_statu(self, statu):
        self.__statu = statu

    # En uygun statünün bulunması için statu_bul metodu
    def statu_bul(self):
        try:
            max_etki = 0
            max_statu = ""
            for statu, yil in self.__tecrube_dict.items():
                etki = 0
                if statu == "mavi yaka":
                    etki = yil * 0.20
                elif statu == "beyaz yaka":
                    etki = yil * 0.35
                elif statu == "yönetici":
                    etki = yil * 0.45

                if etki > max_etki:
                    max_etki = etki
                    max_statu = statu

            self.__statu = max_statu
        except Exception as e:
            print("Hata:", str(e))
            return ""

    # __str__ metotu içinde kullanıcının ad, soyadı ve dictionary ile hesaplanan kişiye
    # en uygun statüyü yazdıran method
    def __str__(self):
        self.statu_bul()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {self.__statu}"
    
