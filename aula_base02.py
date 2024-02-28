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

condicao =  True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome  é {nome}')

    if nome  == 'sair':
        break

print('Saio Loop')


contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')
