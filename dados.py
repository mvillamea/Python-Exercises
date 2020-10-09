import random
[a, b] = random.choices([1, 2, 3, 4, 5, 6], k=2)
print ([a,b])
c = a + b
print("La suma entre los dos dados es ", c)
i = input("¿Desea tirar los dados nuevamente?")
while i == "Si":
    [a, b] = random.choices([1, 2, 3, 4, 5, 6], k=2)
    print ([a,b])
    c = a + b
    print("La suma entre los dos dados es ", c)
    i = input("¿Desea tirar los dados nuevamente?")
else :
    print ("Adiós")







