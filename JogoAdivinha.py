from random import randint
pc=randint(1,100)
print()
resposta=int(input('Vou sortear um número entre "1" à "100", tente adivinhar qual é:  '))

soma=1
while pc != resposta:
    print()
    if resposta > pc:
        soma+=1
        print()
        resposta = int(input('É um número menor, tente novamente..:  '))
        print()
    print()
    if resposta < pc:
        soma += 1
        print()
        resposta = int(input('É um número maior, tente novamente..:  '))
        print()
print()
print('você acertou!!!')
print('Tentativas: {}'.format(soma))