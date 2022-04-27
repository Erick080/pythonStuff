continuar = str('S')
repetições = int(0)
soma = int(0)
maiornum = int(0)
menornum = int(0)



while continuar == 'S':
    num = int(input('Digite o número: '))  
    continuar = str(input('DESEJA CONTINUAR? S/N ')).strip().capitalize()
    soma += num
    repetições +=1
    if repetições == 1:
        maiornum = menornum = num
    else:
        if num > maiornum:
            maiornum = num
        elif num < menornum:
            menornum = num

    

if continuar == 'N':
    print('A média dos seus números é {:.2f}' .format(soma/repetições))
    print('O maior número foi {}\n O menor número foi {}' .format(maiornum,menornum))
