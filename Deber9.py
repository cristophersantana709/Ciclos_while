numero = int(input("Ingrese un numero: "))
a, b = 0, 1
contador = 0
while contador < numero:
 print(a)
 a, b = b, a + b
 contador += 1