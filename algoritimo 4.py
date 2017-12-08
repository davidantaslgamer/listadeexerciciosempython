from math import floor
lista = []
resultado = 1
while True:
    numero = floor(float(input("digite um numero:")))
    if numero > 0:
        break
    elif numero == 0:
        print("forma fatorada de 0 é 1 e o resultado da multiplicaçao entre os fatorais é 0")
        exit()
    else:
        print("numero invalido")
for variavel in range(0,numero):
    subtraçao = numero - variavel
    lista += [subtraçao]
for multiplicação in lista:
    resultado = resultado * multiplicação
print("a forma fatorada de {} é {} e o resultado da multiplicação de seus fatores é {}".format(numero,list(lista),resultado))