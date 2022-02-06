import utils

option = 1

while(option!=4):
    print('1-CPU 1 x CPU 2\n2-Jogador x CPU\n3-Jogador 1 x Jogador 2')
    option = int(input('4-Sair\nOpção: '))

    if(option <= 3 or option >=1):
        end_board = utils.start_game(option=option)
    resultado = utils.testTerminal(end_board)
    if(resultado == utils.VICTORY_O):
        print('Vitória do [o]!')
    elif(resultado == utils.VICTORY_X):
        print('Vitória do [x]!')
    else:
        print('Empate!')
    while(True):
        exit = input('Jogar novamente?\n1.Sim\n2.Não]')
        exit = exit.lower()
        if(exit == 'sim' or exit == 'não' or exit == 1 or exit == 2):
            break
    if(exit=='não' or exit==2):
        break