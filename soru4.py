metin = "Joker is a 2019 film directed by Todd Phillips, which delves into the origin story of one of Batman's most iconic villains. Set in Gotham City, the film follows Arthur Fleck, a struggling comedian with a mental illness who descends into madness and becomes the infamous Joker. The movie explores themes of alienation, society's indifference towards the marginalized, and the consequences of a broken system. Joaquin Phoenix delivers a captivating performance, portraying Arthur's transformation into the Joker with haunting intensity. With its dark and gritty atmosphere, Joker challenges viewers to confront uncomfortable realities and raises questions about the nature of identity, empathy, and the human condition."

aranan_kelime = "Joker"

# metinde kaç kez anahtar kelime geçmektedir? count() fonksiyonunu kullanabiliriz.
tekrar = metin.count(aranan_kelime)
print("aranan kelime metinde", tekrar, "kez gecmektedir.")

# metin içinde aranan anahtar kelimenin hangi indekste olduğunu find() ile bulabiliriz.
# Bu fonksiyon, ilk kelimeyi bulduktan sonra işlevini tamamlayacaktır.
# for dongusu ile metin içinde geçen tüm anahtar kelimelerin indeksini bulabiliriz.
index = -1
for i in range(tekrar):
    index = metin.find(aranan_kelime, index + 1)
    print(f"Joker {i+1} -> Index: {index}")
