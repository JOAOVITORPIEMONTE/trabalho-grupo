import os

def limpar_tela():

    os.system('cls' if os.name == 'nt' else 'clear')

print("======= Soma com 34 =======")
numSomar = int(input("Qual numero você vai somar?\n: "))
soma = int(34 + numSomar)

limpar_tela()
print(f'A soma do seu número é {soma}')