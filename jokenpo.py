from random import randint
from time import sleep
novamente=1
soma1=0
soma2=0
soma3=0
while novamente == 1:
    print('='*40)
    print('Bem vindo ao jogo de JOKENPO!!')
    print('='*40)
    itens=(' ', 'PEDRA' ,'PAPEL', 'TESOURA')
    opcao=int(input('''Escolha o modo de jogo:
[ 1 ] Computador X Humano
[ 2 ] Jubileu X Galo Fantasma
[ 3 ] Humano X Humano
Qual sua opção?  '''))
    while opcao < 1 or opcao >3:
        print()
        print('Opção inválida!! Escolha novamente.')
        print()
        opcao = int(input('''Escolha o modo de jogo:
[ 1 ] Computador X Humano
[ 2 ] Jubileu X Galo Fantasma
[ 3 ] Humano X Humano
Qual sua opção?  '''))
    else:

#opção de humano x computador

        while opcao == 1:
            soma1=0
            soma2=0
            soma3=0
            print('=' * 40)
            print('Bem vindo ao modo Computador X Humano!! ')
            print('=' * 40)
            pc=randint(1,3)
            player=int(input('''Faça sua escolha!!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual sua opção?  '''))
            while player <1 or player>3:
                print()
                print('Jogada inválida!!')
                print()
                player = int(input('''Escolha novamente!!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual sua opção?  '''))
            else:
                print('JO', end=' ')
                sleep(0.5)
                print('KEN', end=' ')
                sleep(0.5)
                print('PO!!!')
                print('='*40)
                if player == 1 and pc == 3 or player==2 and pc==1 or player==3 and pc==2:
                    soma1=+1
                    print('VOCÊ GANHOU!!')
                elif pc == player:
                    soma2=+1
                    print('EMPATE!!')
                else:
                    soma3=+1
                    print('VOCÊ PERDEU!!')
                print('O computador escolheu:',itens[pc])
                print('O jogador escolheu:   ',itens[player])
                print('='*40)
            opcao=int(input('''Jogar novamente?
[ 1 ]Sim
[ 4 ]Não'''))
        print('Placar: Ganhou {} vezes'.format(soma1))
        print('Perdeu  {} vezes'.format(soma3))
        print('Empatou {} vezes'.format(soma2))

#opção de computador x computador

        while opcao == 2:
            print('=' * 40)
            print('Bem vindo ao modo Jubileu X Galo Fantasma!! ')
            pc1 = randint(1, 3)
            pc2 = randint(1, 3)
            print('=' * 40)
            sleep(0.5)
            print('JO', end=' ')
            sleep(0.5)
            print('KEN', end=' ')
            sleep(0.5)
            print('PO!!!')
            if pc1 == 1 and pc2 == 3 or pc1 == 2 and pc2 == 1 or pc1 == 3 and pc2 == 2:
                print('Jubileu venceu!!!')
            elif pc1 == pc2:
                print('EMPATE!!')
            else:
                print('Galo Fantasma venceu!!!')
            print('Jubileu escolheu', itens[pc1])
            print('Galo Fantasma   ', itens[pc2])
            print('=' * 40)
            opcao = int(input('''Jogar novamente?
[ 2 ]Sim
[ 4 ]Não'''))

# opção de humano x humano

        while opcao == 3:
            print('=' * 40)
            print('Bem vindo ao modo Humano X Humano!! ')
            print('''Faça sua escolha!!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual sua opção?  ''')
            jogador1 = int(input('Jogador 1 = '))
            jogador2 = int(input('Jogador 2 = '))
            while jogador1 < 1 or jogador1 > 3 or jogador2 < 1 or jogador2 > 3:
                print()
                print('Jogada inválida!!')
                print()
                print('''Escolha novamente!!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
    Qual sua opção?  ''')
                jogador1 = int(input('Jogador 1 = '))
                jogador2 = int(input('Jogador 2 = '))
            else:
                print('JO', end=' ')
                sleep(0.5)
                print('KEN', end=' ')
                sleep(0.5)
                print('PO!!!')
                print('=' * 40)
                if jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
                    print('Jogador 1 venceu!!')
                elif jogador2 == jogador1:
                    print('EMPATE!!')
                else:
                    print('Jogador 2 venceu!!')
                print('O jogador 1 escolheu:', itens[jogador1])
                print('O jogador 2 escolheu:', itens[jogador2])
                print('=' * 40)
            opcao = int(input('''Jogar novamente?
[ 3 ]Sim
[ 4 ]Não'''))
    novamente=int(input(''' 
[ 1 ] Menu Principal 
[ 2 ] Sair do jogo'''))
    if novamente == 2:
        print('Fim de jogo.')
        break
