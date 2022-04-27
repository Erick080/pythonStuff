maiordeidade = int(0)
homens = int(0)
mulhermaiorde20 = int(0)



while True:
    print('---Cadastro---')
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiordeidade +=1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('M/F ')).lower()
    if sexo == 'm':
        homens +=1
    if sexo == 'f' and idade > 20:
        mulhermaiorde20 += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar?[S/N] ')).lower()
    if continuar == 'n':
        break
print(f'''Foram registrados {maiordeidade} pessoas com mais de 18 anos
{homens} homens
{mulhermaiorde20} mulheres maiores de 20 anos.''')
