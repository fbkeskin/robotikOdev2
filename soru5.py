class Ogrenci:
    def __init__(self, numara, ad, soyad, sinif, yas, cinsiyet):
        self.numara = numara
        self.ad = ad
        self.soyad = soyad
        self.sinif = sinif
        self.yas = yas
        self.cinsiyet = cinsiyet

class OgrenciOtomasyonu:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, numara, ad, soyad, sinif, yas, cinsiyet):
        ogrenci = Ogrenci(numara, ad, soyad, sinif, yas, cinsiyet)
        self.ogrenciler.append(ogrenci)

    def ogrenci_sil(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == numara:
                self.ogrenciler.remove(ogrenci)
                return True
        return False

    def ogrenci_sorgula(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == numara:
                return f"\nNumara: {ogrenci.numara}, Ad: {ogrenci.ad}, Soyad: {ogrenci.soyad}, Sınıf: {ogrenci.sinif}, Yaş: {ogrenci.yas}, Cinsiyet: {ogrenci.cinsiyet}"
        return "Öğrenci bulunamadı."

    def ogrencileri_kaydet(self):
        with open("ogrenci.txt", "w") as file:
            for ogrenci in self.ogrenciler:
                file.write(f"{ogrenci.numara},{ogrenci.ad},{ogrenci.soyad},{ogrenci.sinif},{ogrenci.yas},{ogrenci.cinsiyet}\n")

    def ogrencileri_yukle(self):
        self.ogrenciler = []
        try:
            with open("ogrenci.txt", "r") as file:
                for satir in file.readlines():
                    satir = satir.strip()
                    numara, ad, soyad, sinif, yas, cinsiyet = satir.split(",")
                    ogrenci = Ogrenci(numara, ad, soyad, sinif, yas, cinsiyet)
                    self.ogrenciler.append(ogrenci)
        except FileNotFoundError:
            print("Kayıt dosyası bulunamadı.")

def menu_goster():
    print("\n***** ÖĞRENCİ OTOMASYONU *****")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrenci Sorgula")
    print("4. Çıkış")

otomasyon = OgrenciOtomasyonu()
otomasyon.ogrencileri_yukle()

while True:
    menu_goster()
    secim = input("Seçiminizi yapın (1-4): ")

    if secim == "1":
        numara = input("Numara: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        sinif = input("Sınıf: ")
        yas = input("Yaş: ")
        cinsiyet = input("Cinsiyet: ")
        otomasyon.ogrenci_ekle(numara, ad, soyad, sinif, yas, cinsiyet)
        otomasyon.ogrencileri_kaydet()

        print("\nogrenci kaydedildi.\n")

    elif secim == "2":
        numara = input("Silinecek öğrencinin numarasını giriniz: ")
        if otomasyon.ogrenci_sil(numara):
            otomasyon.ogrencileri_kaydet()
            print("Öğrenci silindi.")
        else:
            print("Öğrenci bulunamadı.")

    elif secim == "3":
        numara = input("Sorgulanacak öğrencinin numarasını giriniz: ")
        bilgi = otomasyon.ogrenci_sorgula(numara)
        print(bilgi)

    elif secim == "4":
        otomasyon.ogrencileri_kaydet()
        print("\nProgramdan çıkılıyor..\n")
        break

    else:
        print("Geçersiz giriş. Tekrar deneyin.")
