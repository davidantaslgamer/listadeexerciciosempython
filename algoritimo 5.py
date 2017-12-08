sequencia = [0,1]
x = int(input("ate que número você quer a seuqncia do carinha lá:"))
marcador = 3
while marcador <= x:
    xz = sequencia[len(sequencia)-1] + sequencia[len(sequencia)-2]
    sequencia += [xz]
    marcador += 1
print("os numeros da sequencia são {}".format(sequencia))