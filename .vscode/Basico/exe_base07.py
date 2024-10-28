'''
Faça uma lista de compra com listas
Usuário deve ter a possibilidade de 
inserir apagar ele estar valores da sua lista
Não permita que o programa quebre com
erros indices inexistentes na  lista
'''
lista = []

while True:

    print('Olá bem-vindo à sua lista de marcados')
    alternativa = input ("Digite as opções: [i]nseri, [a]pagar, [l]lista ")

    if alternativa == ' ':
      print ('desculpe você não inseriu informações')
      continue

    elif alternativa != 'a' and  alternativa != 'i' and alternativa != 'l':
        print('opção inválida')
        continue

    if alternativa in 'i':
       opcao = input ("Digite dado para inserir a lista: ")
       lista.append(opcao)

    elif alternativa in 'a':
        if lista == []:
            print ('está vazia')
            continue
        else:
         opcao = input('digite o índice para apagar na lista:')
         convert = int(opcao)
         del lista [convert]
    
    elif alternativa in 'l':
      if lista == []:
            print ('está vazia')
            continue
      else:
             lista_numerda = list(enumerate(lista))

             for ind, nome in lista_numerda:
              print(ind,nome)

      


    sair = input('deseja sair ? [s]im ou [n]ão: ')
    if sair in 'n':
       continue
    else:
       break



 