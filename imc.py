altura = float (input ('Digite a altura em metros: '))
peso = float (input ('Digite o peso em kg: '))
imc = float (peso/ (altura*altura))

if imc < 18.5:
    print ('VOCE ESTÁ ABAIXO DO PESO COM IMC DE {:.2f}' .format (imc))

elif 18.5 <= imc < 25:
    print ('VOCE ESTÁ NO PESO IDEAL COM IMC DE {:.2f}' .format (imc))

elif 25 <= imc < 30:
    print ('VOCE ESTÁ EM SOBREPESO COM IMC DE {:.2f}' .format (imc))

elif 30 <= imc < 40:
    print ('VOCE ESTÁ EM OBESIDADE COM IMC DE {:.2f}' .format (imc))

elif 40 <= imc:
    print ('VOCE POSSUI OBESIDADE MÓRBIDA COM IMC DE {:.2f}' .format (imc))
