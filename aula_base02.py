#imutáveis
#a variáveis do tipo imutáveis como:
#str, int, float, bool
#quanto temos uma variável, do tipo string int float boleando, 
#é atribuído algum valor a ela.
#Esse valor não muda.
#string int float boleando Elas são métodos caso você aperte "."
#ponto ela aparecerá fun ções para você executar com ela

# repetiçõea com while
#A estrutura de repetição essa é com condição
#Essa estrutura se você não der um fim para ela ela vai se tornar infinita
'''
condicao =  True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome  é {nome}')

    if nome  == 'sair':
        break

print('Saio Loop')


contador = 0

while contador < 10:
    contador +=  1
   # contador = contador + 1

    print(contador)

print('Acabou')

# opedores de atribuição
#  += -= *= /= //= **= %=
valor_cont = 4

valor_cont += 4 
print(f'+= {valor_cont}')
valor_cont -= 4 
print(f'-= {valor_cont}')
valor_cont *= 4 
print(f'*= {valor_cont}')
valor_cont //= 4 
print(f'//= {valor_cont}')
valor_cont /= 4 
print(f'/= {valor_cont}')
valor_cont %= 4 
print(f'%= {valor_cont}')

cont = 0 
while cont <= 30:
    cont +=1

    if cont == 27:
        print("Não exiba 27")
        continue # Ao colocar o continue ele pula o que faz e continua o loop
    print(cont)
    if cont == 29:
        break
    
#estudando laço de repetição com dois While
'''
qtd_linhas = 5
qtd_coluna = 5

linha =1

while linha <= qtd_linhas:
    coluna =1
    while coluna <= qtd_coluna:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha +=1

#  o while esta  na  linha  71 É como se fosse um círculo maior
# o whule  linha  73 outro Círculo.
#Basicamente o que acontece é que o primeiro circo quanto completa 
# a sua volta o outro em seguida executa sua ação.


