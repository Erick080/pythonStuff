num1 = int (input ('Digite o número: '))
num2 = int (input ('Digite o número: '))
option = 0

while option != 5:
    print('''\nEscolha uma opção:
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa''')
    option = int (input (' '))
    if option == 1:
        print('{} + {} = {}' .format(num1,num2,num1+num2))
    elif option == 2:
        print('{} x {} = {}' .format (num1,num2,num1*num2))
    elif option == 3:
        if num1 > num2:
            print('{} é maior que {}' .format(num1,num2))
        elif num2 > num1:
            print ('{} é maior que {}'.format(num2,num1))
        else:
            print('Os números são iguais.')
    elif option == 4:
        num1 = int (input ('Digite o número: '))
        num2 = int (input ('Digite o número: '))


print ('Processo finalizado.')
