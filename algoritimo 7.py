from math import floor
etaria1 = []
etaria2 = []
etaria3 = []
etaria4 = []
etaria5 = []
contador = 1
print("faixa etaria 1 = 0 ate 15 anos")
print("faixa etaria 2 = 16 ate 30 anos")
print("faixa etaria 3 = 31 ate 45 anos")
print("faixa etaria 4 = 46 ate 60 anos")
print("faixa etaria 5 é para quem tem mais de 60 anos")
while contador < 16:
    pessoa = float(input("qual a idade da {} pessoa:".format(contador)))
    pessoa = floor(pessoa)
    if pessoa < 0:
        print("idade invalida")
    elif pessoa >= 0:
        for d in range(0,16):
            if pessoa == d:
                etaria1 += [d]
                contador +=1
            else:
                contador += 0
        for a in range(16,31):
            if pessoa == a:
                etaria2 += [a]
                contador += 1
            else:
                contador += 0
        for v in range(31,46):
            if pessoa == v:
                etaria3 += [v]
                contador += 1
            else:
                contador +0
        for k in range(46,61):
            if pessoa == k:
                etaria4 += [k]
                contador += 1
            else:
                contador += 0
        if pessoa > 60:
                etaria5 += [pessoa]
                contador += 1
print("ha {} pessoas na faixa etaria 1, essas pessoas tem a idade,respectivamente,{} anos".format(len(etaria1),etaria1))
print("ha {} pessoas na faixa etaria 2, essas pessoas tem a idade,respectivamente,{} anos".format(len(etaria2),etaria2))
print("ha {} pessoas na faixa etaria 3, essas pessoas tem a idade,respectivamente,{} anos".format(len(etaria3),etaria3))
print("ha {} pessoas na faixa etaria 4, essas pessoas tem a idade,respectivamente,{} anos".format(len(etaria4),etaria4))
print("ha {} pessoas com mais de 60 anos, essas pessoas tem a idade,respectivamente,{} anos".format(len(etaria5),etaria5))
