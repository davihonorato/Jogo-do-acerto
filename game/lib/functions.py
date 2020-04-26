from random import randint


def pensar():  # Irá gerar, para o 'Computer' um número aleatório entre 0 e 'x'.
    n = randint(1, 3)
    if n == 1:  # Fácil
        num = randint(0, 10)
        print('Pensei em um número entre 0 e 10. Tente acertar!')
    elif n == 2:  # Intermediário
        num = randint(0, 100)
        print('Pensei em um número entre 0 e 100. Tente acertar!')
    else:  # Difícil
        num = randint(0, 1000)
        print('Pensei em um número entre 0 e 1000. Tente acertar!')
    return num


def leiaInt(txt):  # Irá ler uma entrada do usuário e, dependendo, aceitar ou não como um número Inteiro.
    n = str(input(txt))
    if verificar(n):
        num = int(n)
        return num
    else:
        print('Digite um número inteiro válido.')


def verificar(n):  # Verifica se um número indicado é um número Inteiro.
    try:
        num = int(n)  # Tenta tranformar o num é um número Inteiro
    except:
        return False
    else:
        return True


def Aproximidade(player, computer):  # Irá indicar se será necessário digitar um número maior ou menor.
    if player < computer:
        print('Digite um número maior.')
    else:
        print('Digite um número menor.')