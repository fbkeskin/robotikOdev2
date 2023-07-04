import matplotlib.pyplot as plt

# boy ve kilo veri
boy = [167, 160, 155, 180, 170, 163, 160, 172, 159, 190]
kilo = [57, 60, 48, 75, 75, 50, 60, 80, 66, 90]

# verilerin grafik için sıralanması
siralanmis_veriler = sorted(zip(boy, kilo), key=lambda x: x[0])
siralanmis_boy, siralanmis_kilo = zip(*siralanmis_veriler)

# Çizgi grafiği oluşturma
plt.plot(siralanmis_boy, siralanmis_kilo, marker='o')

# eksenlerin isimlendirilmesi
plt.xlabel('Boy (cm)')
plt.ylabel('Kilo (kg)')

plt.title('Öğrencilerin Boy-Kilo Grafiği')

# grafiğin gösterilmesi
plt.show()
