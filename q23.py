n=int(input('numero de funcionários: '))



for i in range(n):
    cod=int(input('digite o código: '))
    horas=float(input('horas trabalhadas:'))
    dependentes=int(input('numero de dependentes: '))

    htotais=12*horas
    dtotais=40*dependentes
    salario=htotais+dtotais
    inss=salario*0.915
    imposto=salario*0.95
    salario_desconto=salario-inss-imposto

    print(f'o total de desconto do INSS é {inss} e do imposto é {imposto}')
    print(f'o salario liquido é igual a {salario_desconto}R$')
