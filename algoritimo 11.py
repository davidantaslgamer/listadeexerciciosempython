palavra = input("digite uma palavra ou frase:").lower()
palavra1 = palavra
if palavra.count(" ") > 0:
    palavra1 = palavra
    palavra = palavra.split()
    palavra = "".join(palavra)
    palavrainversa = palavra[::-1]
    if palavra == palavrainversa:
        print("'{}' é uma frase polindroma".format(palavra1))
    else:
        print("'{}' não é uma palavra polindroma".format(palavra1))
else:
    palavrainversa = palavra[::-1]
    if palavra == palavrainversa:
        print("'{}' é palavra polindroma".format(palavra))
    else:
        print("'{}' não é uma palavra polindroma".format(palavra))
