largura = int(input('diga a largura:'))
largura *= "* "
altura = int(input('diga a altura:'))
usealtura = altura-2
espaço = ""
len = len(largura)-3
espaço = " "*len
print(largura)
marcador = 0
while marcador < usealtura:
    print("*{}*".format(espaço))
    marcador +=1
print(largura)