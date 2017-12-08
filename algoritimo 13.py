n=int(input("digite um numero: "))
valor1="* "
for i in range(0,n+1,1):
    print(i*valor1)
print(" "*n)
valor2="* "
for i in range(n,-1,-1):
    print(i*valor2)
for j in range(0,n):
    k = n-j
    print(" "*j,"*"*(k))
print(" "*n)
for j in range(n-1,-1,-1):
    k = n-j
    print(" "*j,"*"*(k))