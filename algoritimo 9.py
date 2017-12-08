codigos_permitidos = [1,2,3,5,9,0]
total = 0
unidades = 1
def compra(par1):
    global total,unidaes
    totalinterno = par1 * unidades
    total += totalinterno
while True:
    codigo = int(input("digite o codigo do produto:"))
    if codigo in codigos_permitidos:
        if codigo == 0:
            break
        else:
            unidades = int(input("quantas unidaes do produto anterior foram adquiridas?"))
            if codigo == 1:
                compra(0.5)
            if codigo == 2:
                compra(1)
            if codigo == 3:
                compra(4)
            if codigo == 5:
                compra(7)
            if codigo == 9:
                compra(8)
    else:
        print("codigo invalido")
print("total a pagar:",total)