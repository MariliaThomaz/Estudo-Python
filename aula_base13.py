'''
Operação ternária (condicional em uma linha)
#Explicando de uma outra maneira é fazer (if) em uma linha
'''

condicao = 10 == 10
variave = 'Valor' if condicao else 'Outro valor'
print(variave)

digito = 9
novo_digito = digito if digito <=9 else 0
print(novo_digito)

print('Bola' if  True else 'Não é bola')
print('Bola' if  False else 'Não é bola')

#fazer operação ternária, é para ficar esclarecida 
# não a monto há muitos condição
print('Casa' if  True else 'Não tem casa' if True else 'Fim')
print('Casa' if  False else 'Não tem casa' if True else 'Fim')
print('Casa' if  False else 'Não tem casa' if False else 'Fim')
