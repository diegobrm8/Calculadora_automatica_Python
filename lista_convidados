from time import sleep

lista_conv = []


def mostrarMenu():
    opcao = int(input("\n----------MENU----------\n"
                      "[ 1 ] Cadastrar Nome(s)\n"
                      "[ 2 ] Verificar\n"
                      "[ 3 ] ""exibir Lista\n"
                      "[ 4 ] remover\n"
                      "[ 5 ] Deletar Lista\n"
                      "[ 6 ]sair\n"
                      " Sair\nOPÇÃO: "))
    return opcao


def cadastrarNome(nome):
    lista_conv.append(nome)


def verificar(nome):
    if nome in lista_conv:
        print(f'{nome} já esta na lista!')
    else:
        print(f'{nome} não está na lista! ')


def exibirlista():
    lista_conv.sort()
    print('LISTA DE CONVIDADOS:')
    numero = 1
    for nomes in lista_conv:
        print(f'{numero}: {nomes}')
        numero += 1


def remover():
    nome = input('Digite o nome que queira remover:')
    if nome in lista_conv:
        lista_conv.remove(nome)
        print(f'{nome} foi removido')
    else:
        print(f'{nome} já não estava na lista:')


def deletarLista():
    global lista_conv
    lista_conv.clear()
    print("Exclusão sucedida!")


def sair():
    print("SAINDO", end="")
    for c in range(3):
        sleep(0.3)
        print(".", end="")
    exit()


while True:
    opcao = mostrarMenu()
    if opcao == 1:
        cadastrarNome(input("\nNome: ").capitalize())

    elif opcao == 2:
        verificar(input("\nNome: "))

    elif opcao == 3:
        exibirlista()

    elif opcao == 4:
        remover()

    elif opcao == 5:
        deletarLista()

    elif opcao == 6:
        exibirlista()

    elif opcao == 7:
        sair()
    else:
        print("Opção inválida, tente novamente!\n")
