n=int(input('numero de vezes: '))


magro=100000000
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
        peso=magro
        numero_identificação=idmenor
        nome=nome_leve
        
        
print(gordo, idmaior, nome_pesado)
print(peso, numero_identificação, nome)

    

    

