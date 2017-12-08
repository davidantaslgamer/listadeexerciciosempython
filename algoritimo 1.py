from math import ceil,floor
soma = 0
while True:
    numero = floor(float(input("digite um numero:")))
    if numero >= 0:
        break
    elif numero < 0:
        print("numero invalido")
for contador in range(numero,0,-1):
    soma += contador
print(soma)