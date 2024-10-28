'''
Introduz as funções (def) em Python
Funções são trechos de código usado para
Replicar ter terminadas ação ao longo do do seu código
Elas podem receber valores para parâmetros (argumentos)
E retornar valor específico.
Por padrão função em Python retorna none (nada)
'''
'''
def sadacao(nome):
    print(f'Olá, {nome}')
    
sadacao('Marilia')
'''
'''
def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de  {multiplo}, end =' ' ')
    print(resultado)

multiplo_de(16,8)
multiplo_de(15,3)
multiplo_de(10,2)
'''



'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeado recebe apenas um argumento (valor)
'''

#Argumento posicional
def soma(x,y):
    print(f'x={x} y={y}','|','x+y=',x+y)
    
soma(1,2)
#O fato de ser posicional é porque você 
# depende da ordem dos valores

soma(y=20,x=30)
#Esse já é um argumento nomeado
#Você pode colocar argumentos nomeados em casos de não nomeados
# como soma(20,x=30, z=40)
#Mas a partir de que você começa colocar argumentos nomeado
#Você tem que colocar o restante sem argumentos todos nomeados
