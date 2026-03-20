n=int(input('digite o número de habitantes:'))
soma_salario=0
soma_filhos=0
con=0

for i in range(n):
    salario=float(input('digite o valor do seu salário: '))
    filhos=int(input('digite o numero de filhos: '))
    soma_salario+=salario
    soma_filhos+=filhos
    if salario<=1000:
        con+=1

media_salarios=soma_salario/n
media_filhos=soma_filhos/n
percentual=(con/n)*100
print(f'a media de salarios é :{media_salarios}\n a média de filhos é: {media_filhos}\n e o percentual de pessoas que ganham 1000R$ é {percentual:.1f}%')

