from random import randint
#Formatação da tela
print (10*'-=')
print('JOGO DA ADVINHAÇÃO')
#Numero que a máquina escolhe
pc = int (randint(0,10))
#Número que o jogador escolhe
vc = int (input ('\nAdvinhe o número entre 0,10: '))
#Variável acumulável que conta as tentativas do jogador
s = 0

while vc != pc:
    print('Errado, o computador escolheu {}' .format (pc))
    s += 1
    pc = int (randint(0,10))
    vc = int (input ('Tente de novo: '))

if vc == pc:
    print('Você ganhou. Foram precisas {} tentativas' .format (s))
