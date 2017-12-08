# listadeexerciciosempython
1. Escreva um programa que solicite ao usuário um número inteiro e calcule o somatório até o
número fornecido. Mostre o resultado ao usuário. Por exemplo, se o usuário digitar 5, o
programa deve calcular 1+2+3+4+5 e mostrar o resultado 15. Já se o usuário digitar 8, o
programa deve calcular 1+2+3+4+5+6+7+8 e mostrar o resultado 36. Se o usuário digitar zero,
o programa deve mostrar zero como resultado. Se o usuário digitar um número menor que zero
o programa deve mostrar a mensagem “Número Inválido” e solicitar novamente a digitação do
número até que um número maior ou igual a zero seja digitado.
2. Escreva um programa que leia números inteiros digitados do teclado. O programa deve ler os
números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números
digitados, assim como a soma e a média aritmética dos números.
3. Escreva um programa que imprima as tabuadas de 1 até 9 para adição e multiplicação, uma ao
lado da outra. O usuário digitará dois números que limitarão o valor das tabuadas. Por exemplo,
se ele digitar 2 e 8, cada tabuada começará em 2 e terminará em 8. Veja, como ficaria a tabuada
de 2, como exemplo:
2 + 2 = 4 | 2 x 2 = 4
2 + 3 = 5 | 2 x 3 = 6
2 + 4 = 6 | 2 x 4 = 8
2 + 5 = 7 | 2 x 5 = 10
2 + 6 = 8 | 2 x 6 = 12
2 + 7 = 9 | 2 x 7 = 14
2 + 8 = 10 | 2 x 8 = 16
4. Escreva um programa que leia um número inteiro, calcule e imprima o fatorial desde número. O
fatorial de um número N é calculado por N * (N – 1) * (N – 2) * ... * 1. Por exemplo, o fatorial
de 5 é determinado calculando-se 5 * 4 * 3 * 2 * 1 e neste caso o programa deve mostrar o
resultado 120. O fatorial de zero é 1. Caso o usuário digite um número negativo, solicite o
número novamente até que ele digite um número maior ou igual a zero.
5. Escreva um programa que imprima os N primeiros números da sequência de Fibonacci. Esta
sequência é construída da seguinte forma: o primeiro elemento será 0 e o segundo será 1, os
demais elementos são a soma dos dois últimos números anteriores. Assim teremos a sequência
0 1 1 2 3 5 8 ... F(n – 1) + F(n – 2). Resumindo, caso o usuário digite 8, por exemplo, você
deverá imprimir os 8 primeiros números da sequência, ou seja, 0 1 1 2 3 5 8 13.
6. Escreva uma calculadora que realiza as quatro operações aritméticas básicas. Seu programa
deve ler um caractere e dois números reais. O caractere representa a operação que você deve
fazer para os dois números. Se o caractere é + mostre a soma dos números, se – mostre a
subtração, se * mostre a multiplicação e se / mostre a divisão. Após executar a operação
desejada seu programa deve permitir ao usuário fazer outra operação, repetindo o processo. Isso

irá se repetir até que seja digitado o caractere S (maiúsculo ou minúsculo) como operação e
neste caso o programa deverá terminar sem realizar nenhuma outra operação. Abaixo, existe um
exemplo de execução. Primeiro o usuário digita * como operação e 2 e 8 como números, já na
repetição seguinte ele digita s como operação e o programa termina, sem pedir os dois números
ou fazer qualquer operação aritmética. Mostre uma mensagem de erro caso seja digitada uma
operação inválida e continue a execução do programa.
# Menu de operações #
+ para somar;
– para subtrair
* para multiplicar;
/ para dividir;
s para sair.
Escolha a operação: *
Digite o primeiro número: 2
Digite o segundo número: 8
2 * 8 = 16
---------------------------
# Menu de operações #
+ para somar;
– para subtrair
* para multiplicar;
/ para dividir;
s para sair.
Escolha a operação: s
Programa encerrado.
7. Faça um programa que receba a idade de 15 pessoas, calcule e mostre a quantidade de pessoas
em cada faixa etária, seguindo a tabela abaixo:

FAIXA ETÁRIA IDADE
1a Até 15 anos
2a De 16 a 30 anos
3a De 31 a 45 anos
4a De 46 a 60 anos
5a Acima de 60

8. Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um
programa que receba o código e o valor de quinze transações, calcule e mostre:
a) O valor total das compras a vista;
b) O valor total das compras a prazo;
c) O valor total das compras efetuadas;
d) O valor da menor compra;
e) O valor da maior compra.
9. Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao
usuário que digite o código do produto e a quantidade comprada. Podem ser registrados
diferentes produtos durante esse processo. Utilize a tabela de códigos abaixo para obter o preço
de cada produto:

CÓDIGO PREÇO
1 0,50
2 1,00
3 4,00
5 7,00
9 8,00

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
código deve gerar a mensagem de erro “Código Inválido”.
10. Escreva um programa que leia um número N digitado pelo usuário e mostre os N primeiros
números primos. Por exemplo, se for digitado 4, o programa mostrará os quatro primeiros
números primos, sendo 2 3 5 7, neste caso.
11. Faça um programa que leia um texto digitado pelo usuário e diga se ele é palíndromo. Um
palíndromo é uma palavra ou frase que é a mesma lida da esquerda para a direita ou da direita
para a esquerda desconsiderando os espaços. Não se preocupe com sinais ortográficos, acentos
e pontuação. São exemplos de palíndromos:
A torre da derrota
Roma e amor
Ame o poema
Arara
12. Escreva um programa que leia a altura e largura de um retângulo e desenha as bordas do mesmo
usando o símbolo *. Por exemplo, se o usuário digitar 6 para altura e 8 para largura, o programa
deve mostrar:
* * * * * * * *
* *
* *
* *
* *
* * * * * * * *
13. Escreva um programa que leia um inteiro e imprima os seguintes padrões de triângulos, um
abaixo do outro, usando o número lido como tamanho da base e altura do triângulo. Usando o
número 10 como exemplo teríamos:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
