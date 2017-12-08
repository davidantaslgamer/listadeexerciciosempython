def soma():
    numero = float(input("digite o primeiro numero:"))
    numero2 = float(input("digite o segundo numero:"))
    soma = numero + numero2
    print(soma)
def multiplicação():
    numero = float(input("digite o primeiro numero:"))
    numero2 = float(input("digite o segundo numero:"))
    multiplicação = numero*numero2
    print(multiplicação)
def subtração():
    numero = float(input("digite o primeiro numero:"))
    numero2 = float(input("digite o segundo numero:"))
    subtração = numero-numero2
    print(subtração)
def divisão():
    numero = float(input("digite o primeiro numero:"))
    numero2 = float(input("digite o segundo numero:"))
    divisão = numero/numero2
    print(divisão)
lista = ["+","-","*","/","s","S"]
while True:
    while True:
        operação = input("digite '+','-','*','/' para selecionar a operação ou 's' para sair:")
        if operação in lista:
            break
        else:
            print("caractere invalido")
    if operação == "+":
        soma()
    if operação == "-":
        subtração()
    if operação == "*":
        multiplicação()
    if operação == "/":
        divisão()
    if operação == "s" or operação == "S":
        print("programa finalizado")
        exit()