#factorial
def fact(sayi):
  if (sayi == 1):
    return 1;
  return sayi * fact(sayi - 1)

#for control
s = int(input("sayi: "))
print(fact(s))
