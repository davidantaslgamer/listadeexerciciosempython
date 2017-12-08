listadeprimos = [2]
g = 0
teste = 3
n = int(input("digite o numero de primos que você quer:"))
while len(listadeprimos) < n:
    for i in listadeprimos[:]:
        if teste%i >0:
            g += 1
    if g == len(listadeprimos):
        listadeprimos += [teste]
        g = 0
    g = 0
    teste += 1
print("os primeiros {} numeros primos são:{}".format(n,listadeprimos))