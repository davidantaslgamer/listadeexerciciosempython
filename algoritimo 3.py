numerodatabuada = int(input("digite o numero da tabuada:"))
numerofinal = int(input("até onde você quer a tabuada:"))
for contador in range(1,numerofinal+1):
    print("{}+{}={} | {}*{}={}".format(numerodatabuada,contador,numerodatabuada+contador,numerodatabuada,contador,numerodatabuada*contador))