numeros = [44 , 45 , 7, 25, 9, 17 , 18]
num = 0
menor = numeros[0]
while num < len(numeros):
 if numeros[num] < menor:
  menor = numeros[num]
 num += 1
print("El número menor es:", menor)