from game.lib import *

# Programa Principal
print('- - JOGO DO ACERTO - -')

computer = pensar()  # Gerar um número para o 'computer'.
tentativas = 0  # Contagem de quantas tentativas o usuário irá fazer para acertar.

while True:
    player = leiaInt('Digite um número: ')  # Valor digitado pelo usuário.
    tentativas += 1
    if verificar(player):  # Verificação do numéro para evitar que, mesmo colocando uma entrada errada, não execute (ex: ' ').
        if player == computer:
            print('Parabéns! Você acertou.')
            break
        else:
            Aproximidade(player, computer)  # Analisa se o próximo número deve ser maior ou menor que o usuário digitou.
print(f'Total de tentativas: {tentativas}')  # Total de tentativas do usuário.
