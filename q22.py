n=int(input('numero de vezes: '))


magro=float('inf')
gordo=0
idmaior=0
idmenor=0
nome_pesado=' ' 
nome_leve=' '


for i in range( n):
    fichas=int(input(f'digite sua {i+1}° ficha: '))
    numero_identificação=int(input('numero de identificaçã: '))
    nome=(input('nome: '))
    peso=float(input('peso: '))
   
    if peso>gordo:
        gordo=peso
        idmaior=numero_identificação
        nome_pesado=nome
    


    if peso<magro:
        magro=peso
        idmenor=numero_identificação
        nome_leve=nome
    



print(f'o boi mais pesado pesa{gordo}KG e o seu numero de identificação é {idmaior}e o seu nome é {nome_pesado}')

print(f'o boi mais leve pesa {magro}KG e o seu numero de identificação é {idmenor} e o seu nome é {nome_leve}')



    

    

