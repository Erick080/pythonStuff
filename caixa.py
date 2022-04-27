lista = [100,50,20,10,5,2,1]
cont = 0
dinheiro = int(input('Digite quando dinheiro você deseja sacar: '))

while True:
    if dinheiro >= lista[cont]:
        notas = dinheiro//lista[cont]
        print(f'Foram imprimidas {notas} notas de R${lista[cont]}')
        dinheiro = dinheiro % lista[cont]
    cont +=1
    if dinheiro == 0:
        break
print('Processo Finalizado')
