from random import randint
tipodado = int(input('Digite quantos lados tem o dado: '))
vezes = int(input('Quantas vezes vai rolar? '))
numeros = list(randint(1,tipodado) for loop in range(0,vezes))
soma = 0
k = 0
print('Números sorteados:')
for n in numeros:
    print(n, end=' ')

print(f'\nO maior número é {max(numeros)}')
print(f'O menos número é {min(numeros)}')


for loop in range(0,vezes):
        soma = soma + numeros[k]
        k = k+1
    
print("Soma dos números: "soma)
