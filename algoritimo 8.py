transiçõesV = []
transiçõesP = []
listageral = []
soma = 0
somaV = 0
somaP = 0
marcador = 0
while marcador < 16:
    transição = input("qual a transição").lower()
    if transição == str(transição) and (transição == "v" or transição == "p"):
            valor = int(input("digite o valor da transição:"))
            if transição == "p":transiçõesP += [valor] ; somaP += valor
            elif transição == "v":transiçõesV += [valor] ; somaV += valor
            marcador += 1
            soma += valor
            listageral += [valor]
            maior = valor
            menor = valor
    else:print("transição invalida")
for i in listageral:
    if maior < i:maior = i
    elif menor > i:menor = i

print("valores transicionados por meio de V:{}, e soma {}".format(transiçõesV,somaV))
print("valores transicionador por meio de P:{}, e a soma {}".format(transiçõesP,somaP))
print("soma total de todos os meios:{}".format(somaV+somaP))
print("menor valor detectado:{}".format(menor))
print("maior valor detectado:{}".format(maior))