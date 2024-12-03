# turkstudentcoodev2

todolist =
görev_yöneticisi = GörevYöneticisi()
görev_yöneticisi.görev_ekle("Alışveriş yapmak")
görev_yöneticisi.görev_ekle("Kitap oku")
görev_yöneticisi.görevi_tamamla("Alışveriş yapmak")
görev_yöneticisi.görevleri_listele()
görev_yöneticisi.görevleri_dosyaya_kaydet("görevler.txt")
görev_yöneticisi.görevleri_dosyadan_yükle("görevler.txt")

hava durumu=
hava_durumu = HavaDurumu()
hava_durumu.şehir_ekle("Istanbul", 8)
hava_durumu.şehir_ekle("Antalya", 25)
hava_durumu.şehir_listele()
hava_durumu.sıcaklık_güncelle("Istanbul", 12)
hava_durumu.şehir_sorgula("Antalya")
hava_durumu.tavsiye_ver(8)

alışveriş sepeti uygulaması =
sepet = Sepet()
sepet.ürün_ekle("Elma", 5, 3)
sepet.ürün_ekle("Laptop", 5000, 1)
sepet.sepeti_listele()
sepet.ürün_çıkar("Elma")
sepet.toplam_tutar()
