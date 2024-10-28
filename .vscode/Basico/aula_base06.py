#lista em python
#Tipo liste mutável
#Suportar vários valores de qualquer tipo
#Conhecimento reutilizáveis índice e fatiamento
#Métodos úteis: append inste, pop, del certo e extend, +

strig = 'ABCDE'
#         0     1       2       3    4
#         -5   -4      -3      -2   -1
lista = [123, True, 'Marilia', 1.2, []]

print (lista[2].upper(), type(lista[2]))
print(lista, type(lista)) 

#O diferencial de usar a lista que os valores pode ser mudados
lista[2] ='Marilia Thomaz' # Atribuindo um novas coisas pra lista

print(lista)

# lista
# Create: Criar, Read: Ler,  Update= Atualizar e Delete 
# Isso quer dizer que a lista pode ler alterar apagar e
#  reconhecido como abreviação CRUD

vendoLista =  [10, 20 ,40, 50]
print(vendoLista)
vendoLista[2] =30
print(vendoLista)
del vendoLista [3] # Ao deletar um item da lista,
#O que acontece que a lista se organiza os seus índice
#Uma das recomendações é evitar fazer essas delete da lista 
# Pois essa mudança de índice pode te atrapalhar
print(vendoLista)

#Adicionar mais coisas Na lista usar  Um método para fazer uma nova ação
vendoLista.append(50)#Esse valor que será atribuído para lista será no final dela
print(vendoLista)

#Para remover o último item da lista você usa
vendoLista.pop()
print(vendoLista)

#Para limpar a lista
vendoLista.clear()
print(vendoLista)

vendoLista = [78,56,11,51,32,75,21,32,14,25]
print(vendoLista)

#Apagando o último item da lista
vendoLista.pop()
print(vendoLista)

#Informando qual índice pode ser apagado
vendoLista.pop(2)
print(vendoLista)

#Inserir algum dado em algum índice
vendoLista.insert(0,99)#Ao usar esse método você tem que passar 2 argumentos
#O primeiro argumento é o índice, O segundo argumento é o valor atribuído para lista
print(vendoLista)

vendoLista.insert(100,88)
#Sabemos que nossa lista é pequena e ela não tenho uma dimensão da qual eu coloquei
print(vendoLista)
#É observamos que a quando você coloca um índice maior automaticamente o PY 
#Tem um mecanismo de colocar isso como um o valor atribuído no final da lista
'''print(vendoLista[100])'''#Mas caso você for consultar esse dado na no índice 100
#O py tom mostra um erro.
#Este erro é devido que se formos observarmos ele coloca para o final da lista ordenando os dados
#Isto quer dizer se você consultar Indicando o índice correto contando de zero até 9 no caso do exemplo
#Você conseguirá ver o valor que foi atribuído àquele espaço da lista.
print(vendoLista[9])

#Concatenação de lista
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)

#Outro jeito de colocar fazer uma concatenação de dados é
#  colocar os itens da lista em outra lista
lista_d = lista_a.extend(lista_b)
print(lista_d)#O fato do de da none que é valor vazio é porque não foi dado nada pra essa variável mas sim foi mudado diretamente na lista_a
print(lista_a)