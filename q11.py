limite_inferior=int(input('digite o limite inferior: '))
limite_superior=int(input('limite superior: '))


for i in range(limite_inferior, limite_superior+1):
    if i%2==0:
        print(i)
    elif i%3==0:
        print(i)
    elif i%5==0:
        print(i)
    elif i%7==0:
        print(i)
        