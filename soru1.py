# koordinatları verilen üçgenin alanı matris çarpımından gelir.
# (x1,y1),(x2,y2),(x3,y3)
# alan= [x1(y2-y3)+x2(y3-y1)+x3(y1-y2)]/2

#ucgenalani
def ucgen_alani(x1, y1, x2, y2, x3, y3):
  return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
  #abs = mutlak deger

#sonradan verilen ikili icinde mi
def icinde_mi(x, y, x1, y1, x2, y2, x3, y3):
  A = ucgen_alani(x1, y1, x2, y2, x3, y3)
  alt_ucgen1 = ucgen_alani(x, y, x2, y2, x3, y3)
  alt_ucgen2 = ucgen_alani(x1, y1, x, y, x3, y3)
  alt_ucgen3 = ucgen_alani(x1, y1, x2, y2, x, y)

  #eger verilen ikili, ucgenin icindeyse alt ucgenlerin toplamı ana ucgenin alanına esit olacaktir.
  if (A == alt_ucgen1 + alt_ucgen2 + alt_ucgen3):
        return True
  else:
        return False

#A ucgeni koordinatlari
x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4

#kullanicidan istenilen ikili
x = float(input("x: "))
y = float(input("y: "))

kontrol = icinde_mi(int(x), int(y), int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
if (kontrol == True):
    print("result True")
else:
    print("result False")

