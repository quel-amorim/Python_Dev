valores = [110 , 290 , 400 , 0 , 80] # Exemplo
valores02 = [0 , 90 , 4 , 3 , 8] # Exemplo

valores.append(99) # Adicionar um novo valor

valores.extend(valores02) # Pegar todos os elementos da matriz valores02 para o final da matriz valores

valores.pop() # Remover tudo e retorna vazio
valores.pop(1) # Remover apenas a matriz inserida no exemplo 1

valores.insert(7, 248) # fazer um novo valor no indico 7 com valor 248


tamanho = int(input('Quantidade ?'))

for i in range(tamanho):
    consumo = float(input(f'Informe a {i+1}a.  medicao de consumo :'))
    total = consumo
    total += consumo
    media = total / tamanho
    i+=1
    

print(f'Média das {tamanho} medicoes de consumo : {media}')

numeros = ""
for contador in range(0 , 202, 2):
    numeros += str(contador) + ","
print(numeros)