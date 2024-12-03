class Ürün:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad  
        self.fiyat = fiyat  
        self.miktar = miktar  

    def __str__(self):
        return f"{self.ad} - {self.miktar} adet - {self.fiyat} TL"  


class Sepet:
    def __init__(self):
        self.ürünler = []  

    def ürün_ekle(self, ad, fiyat, miktar):
        ürün = Ürün(ad, fiyat, miktar)
        self.ürünler.append(ürün)  

    def ürün_çıkar(self, ad):
        for ürün in self.ürünler:
            if ürün.ad == ad:
                self.ürünler.remove(ürün)
                print(f"{ad} ürün sepette çıkarıldı.")
                return
        print(f"{ad} ürünü sepette bulunamadı.")  

    def sepeti_listele(self):
        if not self.ürünler:
            print("Sepetiniz boş.")
        else:
            for ürün in self.ürünler:
                print(ürün)  

    def toplam_tutar(self):
        toplam = sum(ürün.fiyat * ürün.miktar for ürün in self.ürünler)
        print(f"Toplam tutar: {toplam} TL")  


if __name__ == "__main__":
    sepet = Sepet()

    sepet.ürün_ekle("Elma", 5, 3)
    sepet.ürün_ekle("Armut", 8, 2)
    sepet.ürün_ekle("Muz", 7, 1)

    print("Sepetinizdeki Ürünler:")
    sepet.sepeti_listele()

    sepet.toplam_tutar()

    sepet.ürün_çıkar("Armut")

    print("\nGüncel Sepet:")
    sepet.sepeti_listele()

    sepet.toplam_tutar()
