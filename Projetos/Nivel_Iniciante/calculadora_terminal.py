"""Fazer um versão simples ,não usando ela como uma classe"""

#Começar

def somar():
    print(f'{n1} + {n2} = {n1+n2}')

def sub():
    print(f'{n1} - {n2} = {n1-n2}')

def div():
    if n2 !=0:
        print(f'{n1} / {n2} = {n1/n2}')
    else:
        print('Divisão por zero')

def mult():
    print(f'{n1} x {n2} = {n1*n2}')

while True:
    print('-=-'*7)
    print('Menu')
    print('-=-'*7)
    try:
        n1 = float(input('1° Valor:'))
        n2 = float(input('2° Valor:'))
        
    except ValueError:
        print('Erro de sintase')
        continue

    print('1.Começar Operações')
    escolha = input('Escolha :')

    if escolha == "1":
        somar()
        sub()
        div()
        mult()
        break
    else:
        continue


#Programa feito com sucesso !