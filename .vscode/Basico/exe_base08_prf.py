import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')  # ou 'cls' se for no Windows
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')

    elif opcao == 'l':
        os.system('cls')  # ou 'cls' se for no Windows

        if len(lista) == 0:
            print('Nada para listar.')
        else:
            for i, valor in enumerate(lista):
                print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')
