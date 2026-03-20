n=int(input('digite o numero de eleitores: '))

escolha=0
candidato1=0
candidato2=0
candidato3=0
total_votos=0
voto_branco=0
voto_nulo=0
vencedor=0

for i in range(n):
    voto=int(input('digite o numero do seu voto: '))

    if voto==1:
        candidato1=voto
    elif voto==2:
        candidato2=voto
    elif voto==3:
        candidato3=voto
    elif voto==9:
        voto_branco=voto
        print('voce votou nulo')
    elif voto==0:
        voto_nulo=voto
        print('voce votou em branco')
    else:
        print('esse candidato não existe')

    if candidato1>candidato2 and candidato1>candidato3:
        vencedor=candidato1
    elif candidato2>candidato1 and candidato2>candidato3:
        vencedor=candidato2
    elif candidato3>candidato1 and candidato3>candidato2:
        vencedor=candidato3
    else:
        print('a eleição resultou em enpate!')

    
print(f'o total de votos recebidos pelo candidato um foram {candidato1}')
print(f'o total de votos recebidos pelo candidato dois foram {candidato2}')
print(f'o total de votos recebidos pelo candidato três foram {candidato3}')
print(f'o total de votos nulos foram {voto_branco}')
print(f'o total de votos em branco {voto_nulo}')
print(f'o vencedor da eleição foi o candidato {vencedor}')



    

