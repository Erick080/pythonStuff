#modificacao teste
from datetime import date

ano = date.today().year
nasc = int (input ('Digite o ano de nascimento:'))
idade = int (ano - nasc)

if idade < 18:
    dif = int (18 - idade)
    print ('Ainda falta[m] {} ano[s] para o alistamento, em {}.' .format (dif, ano + dif))

elif idade > 18:
    dif = int (idade - 18)
    print ('O alistamento está {} ano(s) atrasado(s), deveria ter sido feito em {}.' .format (dif, ano - dif))

elif idade == 18:
    print ('O alistamento deve ser feito este ano')
