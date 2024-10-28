#Explicando a importância de usar um laço de repetição while Em casos de repetições da 
# qual você não sabe a quantidade de vezes que irá precisar executar alguma ação
#  eis a necessidade de você usar esse laço de repetição "While"
#Como esse exemplo de uma verificação de senha que está abaixo
''' 
senha_salva = '123456'
senha_digitada = ''
repeticoes =0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes +=1

print(repeticoes)
print('Aquela ação acima pode ter repetições infinitas')
'''
# Usando o laço de repetição for

texto = 'Eu amo voce'

for letra in texto:
    print(letra) #letra  É o inteirador 

#For + Range
#rage -> range(start, stop,  step)
print('RANGE')
numeros = range(0,100, 8) 
for numero in numeros:
    print(numero)


for i  in range(10):
    if i ==2:
        print('i é  2, pulando ')
        continue
    if i == 8:
        print('e é 8, sewy else não execvuta ')
        break
    
    for j in range(1,  3):
        print(i,j)
else:
    print('For completo com sucesso! ')


# Lista com laço de repetição for

lista = ['Pedro','Giovana','Catarina']
#para  ver Indeces
indices =  range(len(lista))

for indice in  indices:
    
    print(indice, lista[indice])
   


#Outra maneira de numerar 
lista_nume = ['Pedro','Giovana','Catarina']

lista_numerda = enumerate(lista_nume) #Esse método recebe alista ele inúmera a lista
print(lista_numerda)#elocal de  memoria É o índice da memória Integrator

print(next(lista_numerda))
#usando  o next Irá pegar o primeiro valor
#Se você observar agora nós temos tupla

#lista_numerda = list(enumerate(lista_nume))

#Você observa que agora a gente tem uma Tupla
#tem  dois valore índice e o nome
'''for item in lista_numerda:
    ind, nome =  item
    print(ind,nome)
'''


#Outra maneira é colocar o índice junto com o nome dentro do for
for ind, nome in lista_numerda:
     print(ind,nome)