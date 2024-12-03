class Görev:
    def __init__(self, ad):
        self.ad = ad
        self.tamamlandi = False

    def tamamla(self):
        self.tamamlandi = True

    def __str__(self):
        return f"{self.ad} - {'Tamamlandı' if self.tamamlandi else 'Tamamlanmadı'}"

class GörevYöneticisi:
    def __init__(self):
        self.görevler = []

    def görev_ekle(self, görev_adı):
        görev = Görev(görev_adı)
        self.görevler.append(görev)

    def görevleri_listele(self):
        for görev in self.görevler:
            print(görev)

    def görevi_tamamla(self, görev_adı):
        for görev in self.görevler:
            if görev.ad == görev_adı:
                görev.tamamla()

    def görevi_sil(self, görev_adı):
        self.görevler = [görev for görev in self.görevler if görev.ad != görev_adı]

    def görevleri_dosyadan_yükle(self, dosya_adı):
        try:
            with open(dosya_adı, 'r', encoding='utf-8') as dosya:
                for satır in dosya:
                    görev_adı, tamamlandi_str = satır.strip().split(',')
                    görev = Görev(görev_adı)
                    if tamamlandi_str.lower() == 'true':
                        görev.tamamla()
                    self.görevler.append(görev)
        except FileNotFoundError:
            print(f"{dosya_adı} dosyası bulunamadı.")

    def görevleri_dosyaya_kaydet(self, dosya_adı):
        with open(dosya_adı, 'w', encoding='utf-8') as dosya:
            for görev in self.görevler:
                dosya.write(f"{görev.ad},{görev.tamamlandi}\n")

    def tamamlanan_görevleri_göster(self):
        for görev in self.görevler:
            if görev.tamamlandi:
                print(görev)

    def tamamlanmayan_görevleri_göster(self):
        for görev in self.görevler:
            if not görev.tamamlandi:
                print(görev)

if __name__ == "__main__":
    görev_yöneticisi = GörevYöneticisi()

    görev_yöneticisi.görev_ekle("Alışveriş yapmak")
    görev_yöneticisi.görev_ekle("Kitap oku")

    görev_yöneticisi.görevi_tamamla("Alışveriş yapmak")

    print("Görevler:")
    görev_yöneticisi.görevleri_listele()

    görev_yöneticisi.görevleri_dosyaya_kaydet("görevler.txt")

    yeni_görev_yöneticisi = GörevYöneticisi()
    yeni_görev_yöneticisi.görevleri_dosyadan_yükle("görevler.txt")

    print("\nYüklenen Görevler:")
    yeni_görev_yöneticisi.görevleri_listele()
