valores = []

while True:
    num = int(input('Digite o número: '))
    if num not in valores:
        valores.append(num)
    if num in valores:
        print('O número já foi digitado, não vou adicionar.')
    cont = str(input('Deseja continuar? [s/n] '))
    while cont not in 'SsNn':
        cont = str(input('Resposta inválida, deseja continuar? [s/n]'))
    if cont in 'Nn':
        break
   
valores.sort()
print(f'A lista em ordem crescente: {valores}')
