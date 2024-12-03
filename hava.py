class Şehir:
    def __init__(self, ad, sıcaklık):
        self.ad = ad  
        self.sıcaklık = sıcaklık  

    def __str__(self):
        return f"{self.ad}: {self.sıcaklık}°C"  


class HavaDurumu:
    def __init__(self):
        self.şehirler = []  

    def şehir_ekle(self, ad, sıcaklık):
        şehir = Şehir(ad, sıcaklık)
        self.şehirler.append(şehir)  

    def şehir_listele(self):
        if not self.şehirler:
            print("Hiç şehir eklenmemiş.")
        else:
            for şehir in self.şehirler:
                print(şehir)  

    def tavsiye_ver(self, sıcaklık):
        if sıcaklık < 0:
            print("Soğuk, sıkı giyinin.")
        elif 0 <= sıcaklık <= 15:
            print("Serin, mont almayı unutmayın.")
        else:
            print("Hava güzel, rahat giyin.")  

    def sıcaklık_güncelle(self, ad, yeni_sıcaklık):
        for şehir in self.şehirler:
            if şehir.ad == ad:
                şehir.sıcaklık = yeni_sıcaklık  
                print(f"{ad} şehri için sıcaklık güncellendi: {yeni_sıcaklık}°C")
                return
        print(f"{ad} şehri bulunamadı.")  

    def şehir_sorgula(self, ad):
        for şehir in self.şehirler:
            if şehir.ad == ad:
                print(şehir)  
                return
        print(f"{ad} şehri bulunamadı.")  


if __name__ == "__main__":
    hava_durumu = HavaDurumu()

    hava_durumu.şehir_ekle("İstanbul", 22)
    hava_durumu.şehir_ekle("Ankara", 12)
    hava_durumu.şehir_ekle("Erzurum", -5)

    print("Şehirler:")
    hava_durumu.şehir_listele()

    print("\nTavsiye:")
    hava_durumu.tavsiye_ver(22)  

    hava_durumu.sıcaklık_güncelle("Ankara", 18)

    print("\nGüncel Şehirler:")
    hava_durumu.şehir_listele()

    print("\nŞehir Sorgulama:")
    hava_durumu.şehir_sorgula("Erzurum")
    hava_durumu.şehir_sorgula("İzmir")  