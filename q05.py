n=int(input('numero: '))
resultado=1


for i in range(1,n+1):
    resultado=resultado*i

print(f'o fatorial de {n} é {resultado}')