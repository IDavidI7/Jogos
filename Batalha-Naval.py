import os

nLinhas = nColunas = 20
posicoes_horizontais = '    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20'
posicoes_verticais = (
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T')
# navios = [['Porta-Aviao', 4, 3, '🚢'], ['Cruzador', 3, 4, '🛥️'], ['Fragata', 2, 5, '🚤']]
navios = [['Porta-Aviao', 4, 1, '🚢'], ['Cruzador', 3, 0, '🛥️'], ['Fragata', 2, 0, '🚤']]
posicoes_atacadas = []
acertos = 0


def gera_tabuleiro():
    tabuleiro = ['🌊'] * nLinhas
    for linha in range(nLinhas):
        tabuleiro[linha] = ['🌊'] * nColunas
    return tabuleiro


def print_tabuleiro(tabuleiro):
    print(posicoes_horizontais)
    for linha in range(nLinhas):
        linha_tabuleiro = posicoes_verticais[linha] + '  '
        for posicao in tabuleiro[linha]:
            linha_tabuleiro += posicao
            linha_tabuleiro += '  '
        linha_tabuleiro += posicoes_verticais[linha]
        print(linha_tabuleiro)
        linha_tabuleiro = ''
    print(posicoes_horizontais)


def menu():
    menu = 'Voce possui'
    if (navios[0][2] > 0):
        menu += ', ' + f'{navios[0][2]}' + ' Porta-Aviao(oes)'
    if (navios[1][2] > 0):
        menu += ', ' + f'{navios[1][2]}' + ' Cruzador(es)'
    if (navios[2][2] > 0):
        menu += ', ' + f'{navios[2][2]}' + ' Fragata(s)'
    menu += '.'
    print(menu)
    print('Qual voce prefere colocar no tabuleiro agora ?')
    if (navios[0][2] > 0):
        print('1 - Porta Aviao')
    if (navios[1][2] > 0):
        print('2 - Cruzador')
    if (navios[2][2] > 0):
        print('3 - Fragata')
    print('11 - Para sair do jogo')


def pega_posicao(defesa, navio=0):
    if (defesa):
        print(f'O(A) {navios[navio][0]} ocupará {navios[navio][1]} posicoes.')
        print(f'A posicao escolhida e {navios[navio][1] - 1} a direita dela.')
    print('Informe a linha (A-T) : ')
    linha = acha_linha(input().upper().strip())
    print('Informe a coluna (1-20)')
    coluna = int(input().strip()) - 1
    return [linha, coluna]


def acha_linha(letra):
    for index in range(nColunas):
        if (posicoes_verticais[index] == letra):
            return index
    return -1


def valida_posicao(tabuleiro, navio, posicao):
    linha, coluna = posicao
    if (linha == -1 or coluna > 18 or coluna < 0 or coluna + navios[navio][1] - 1 > 19):
        return False
    for index in range(navios[navio][1]):
        if (tabuleiro[linha][coluna + index] != '🌊'):
            return False
    return True


def valida_ataque(posicao):
    linha, coluna = posicao
    if linha == -1 or coluna > 18 or coluna < 0:
        return False
    for index in range(len(posicoes_atacadas)):
        if posicoes_atacadas[index][0] == linha and posicoes_atacadas[index][1] == coluna:
            return False
    return True


def bota_navio_no_tabuleiro(tabuleiro, navio, posicao):
    linha, coluna = posicao
    for index in range(navios[navio][1]):
        tabuleiro[linha][coluna + index] = navios[navio][3]
    navios[navio][2] -= 1


def ataca_posicao(tabuleiro_ataque, tabuleiro_defesa, posicao):
    linha, coluna = posicao
    global acertos
    if tabuleiro_defesa[linha][coluna] != '🌊':
        tabuleiro_ataque[linha][coluna] = '💥'
        acertos += 1
    else:
        tabuleiro_ataque[linha][coluna] = '❌'
    posicoes_atacadas.append([linha, coluna])


def reseta_tabuleiro():
    global acertos
    global posicoes_atacadas
    acertos = 0
    posicoes_atacadas = []

    return [['Porta-Aviao', 4, 3, '🚢'], ['Cruzador', 3, 4, '🛥️'], ['Fragata', 2, 5, '🚤']]


def defesa():
    while True:
        if (navios[0][2] == 0 and navios[1][2] == 0 and navios[2][2] == 0):
            break

        menu()

        escolha_usuario = int(input()) - 1
        while escolha_usuario not in [0, 1, 2, 10]:
            print('Escolha invalida, tente novamente.')
            escolha_usuario = int(input()) - 1

        if (escolha_usuario == 10):
            break

        print_tabuleiro(tabuleiro_defesa)
        escolha_posicao = pega_posicao(True, escolha_usuario)

        while not valida_posicao(tabuleiro_defesa, escolha_usuario, escolha_posicao):
            print('Formato invalido, tente novamente.')
            escolha_posicao = pega_posicao(True, escolha_usuario)

        bota_navio_no_tabuleiro(tabuleiro_defesa, escolha_usuario, escolha_posicao)
        print_tabuleiro(tabuleiro_defesa)


while True:

    tabuleiro_defesa = gera_tabuleiro()

    while True:
        defesa()
        if (navios[0][2] != 0 or navios[1][2] != 0 or navios[2][2] != 0):
            break
        print('Você deseja refazer sua jogada ?')
        print('1 - Sim')
        print('2 - Nao')
        jogar_novamente = int(input())
        while jogar_novamente not in [1, 2]:
            print('Valor invalido, tente novamente.')
            jogar_novamente = int(input())

        if jogar_novamente == 2:
            break
        else:
            navios = reseta_tabuleiro()
            os.system('cls||clear')

    os.system('cls||clear')
    tabuleiro_ataque = gera_tabuleiro()

    while True:
        if (navios[0][2] != 0 or navios[1][2] != 0 or navios[2][2] != 0):
            break
        print('Escolha a posição que deseja atacar:')
        print_tabuleiro(tabuleiro_ataque)
        print()
        escolha_posicao = pega_posicao(False)

        while not valida_ataque(escolha_posicao):
            print('Posicao invalida ou ja escolhida, tente novamente.')
            escolha_posicao = pega_posicao(False)

        ataca_posicao(tabuleiro_ataque, tabuleiro_defesa, escolha_posicao)

        if (acertos == 4):
            print_tabuleiro(tabuleiro_ataque)
            print('Voce ganhou !!!!')
            print(f'Voce jogou {len(posicoes_atacadas)} vezes')
            break

    print('Voce deseja jogar novamente ?')
    print('1 - Sim')
    print('2 - Nao')
    jogar_novamente = int(input())
    while jogar_novamente not in [1, 2]:
        print('Valor invalido, tente novamente.')
        jogar_novamente = int(input())

    if jogar_novamente == 2:
        break
    else:
        navios = reseta_tabuleiro()
        os.system('cls||clear')



