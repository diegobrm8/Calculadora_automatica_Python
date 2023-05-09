def ler_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    return num1, num2

def somar(num1, num2):
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

def multiplicar(num1, num2):
    resultado = num1 * num2
    print(f"{num1} x {num2} = {resultado}")

def subtrair(num1, num2):
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

def mostrar_menu():
    print('''Escolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Subtrair
    [4] Informar novos números
    [5] Sair do programa''')
    opcao = int(input("Opção: "))
    return opcao

def main():
    num1, num2 = ler_numeros()
    opcao = 0
    while opcao != 5:
        opcao = mostrar_menu()
        if opcao == 1:
            somar(num1, num2)
        elif opcao == 2:
            multiplicar(num1, num2)
        elif opcao == 3:
            subtrair(num1, num2)
        elif opcao == 4:
            num1, num2 = ler_numeros()
        elif opcao == 5:
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == '__main__':
    main()
