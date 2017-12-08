from math import floor
lista = []
soma = 0
while True:
    numero = floor(float(input("digitr um numero:")))
    if numero == 0:
        break
    else:
        soma += numero
        lista += [numero]
media = soma/len(lista)
print(len(lista))
print(soma)
print(media)