n=int(input('escreva o valor de n: '))
limite_inferior=int(input('digite o limite inferior: '))
limite_superior=int(input('digite o limite superior: '))

for i in range(limite_inferior, limite_superior+1):
    if i%n==0:
        print(i)

