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

for nome in  lista:
    print(nome)