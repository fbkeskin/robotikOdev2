#girilen sayının tam bolenlerini bulan func
def tamSayiBolenBulma(sayi):
    bolenListesi=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            bolenListesi.append(-i) #negatif tam bolen
            bolenListesi.append(i)  #pozitif tam bolen
            bolenListesi.sort()     #degerleri siralama
    return bolenListesi

#kullanıcıdan sayı isteme
sayi = int(input("sayi: "))
print(tamSayiBolenBulma(int(sayi)))

