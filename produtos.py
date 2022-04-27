somapreço = int(0)
somamaiordemil = int(0)
menornome = ' '
menorpreço = int(0)
cont = int(0)
while True:
    nome = str (input('Digite o nome do produto: '))
    preço = int (input('Digite seu preço: '))
    somapreço += preço
    cont += 1
    if preço > 1000:
        somamaiordemil +=1
    if cont == 1:
        menornome = nome
        menorpreço = preço
    else:
        if preço < menorpreço:
            menornome = nome
            menorpreço = preço
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).lower()
    if continuar == 'n':
        break
print(f''' A soma total dos preços dos produtos foi {somapreço}
A soma do número de produtos mais caros que R$1000 foi {somamaiordemil}
O produto mais barato foi {menornome}, custando {menorpreço} reais
FIM''')
