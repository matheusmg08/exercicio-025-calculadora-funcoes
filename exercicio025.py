"""
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da
soma, o novo estado da memória passa a ser 8.
Estado da memória: 0
Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
Qual opção você deseja?
"""
#Função para somar 
def somar(memoria, numero):
    return memoria + numero
#Função para subtrair
def subtrair(memoria, numero):
    return memoria - numero
#Função para multiplicar
def multipicar(memoria, numero):
    return memoria * numero
#Função para dividir
def dividir(memoria, numero):
    if numero == 0:
        print("Não é possível dividir nenhum número por zero.")
        return memoria
    return memoria / numero

#Função para chamar o menu
def menu():
    memoria = 5
    while True:
        print("=" *40)
        print(f"A memória vale {memoria}")
        print("1- Somar")
        print("2- Subtrair")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Limpar memória")
        print("6- Sair do programa...")
        print("=" *40)
        opcao = input("Escolha a opção: ")
        print("=" *40)

        if opcao == "1":
            numero = int(input(f"Digite o número que deseja somar com o número {memoria}: "))
            memoria = somar(memoria, numero)
        elif opcao == "2":
            numero = int(input(f"Digite o número que deseja subtrair do número {memoria}: "))
            memoria = subtrair(memoria, numero)
        elif opcao == "3":
            numero = int(input(f"Digite o número que deseja multiplicar com o número {memoria}: "))
            memoria = multipicar(memoria, numero)
        elif opcao == "4":
            numero = int(input(f"Digite o número que deseja dividir com o número {memoria}: "))
            memoria = dividir(memoria, numero)
        elif opcao == "5":
            memoria = 0
        elif opcao == "6":
            print("Saindo do programa...")
        else:
            print("Opção inválida, tente novamente!")

if __name__=='__main__':
    menu()






    
















        #Funçao para o menu


    

