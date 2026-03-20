n = int(input('Digite um número: '))

a=0
b=1
print(a, b, sep='\n')


for i in range(1, n+1):
    proximo=a+b
    a=b
    b=proximo
    print(proximo)