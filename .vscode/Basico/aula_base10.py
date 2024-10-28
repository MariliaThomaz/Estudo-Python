'''
split e join com  list  e str
split - dicide uma strig
join - une uma  string
'''

frase = 'Olha só que,     coisa interessante'
print(f'Frase: {frase}')
lista_palavras = frase.split(',')
#o metodo split pode infomar como quer que faça  a a separação das palavras  
#o que você tem que fazer é passar um argumento
print(f'Palavra sepada {lista_palavras}')

#tirando os espaço da frase
# usando um metodo Strip
lista_frase = []
for i, frase in  enumerate(lista_palavras):
    lista_frase.append(lista_palavras[i].strip())
    #tira o espaço da direita --> rstrip()
    #tira o espaço da esquerda--> lstrip()
    
print(f'Sem espaçoa: {lista_frase}')


#metodo de String o Join
frase_unida = ' # '.join(lista_frase)
print(f'Uniudo: {frase_unida}')

    