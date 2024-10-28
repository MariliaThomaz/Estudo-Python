#desempacotamento e chamda  de funlção 

lista = ['Maria', 'Helana', 1,2,3, 'Eduarda']

p, b, *_, ap, u =lista
# O desempacotamento, Está relacionado a ordem
# A usar (*- ) Você tira um intervalo do tempo e  tambem colocando limite
#print(p, u)

#fazer uma  interção intena
for nome in lista:
    print(nome, end=' ', sep=' ' )#Isto é o desempacotamento em chamada de função
    #end Quebra de linha
    #sep Espaço
    
#Outra maneira de desempacotar
print(*lista)

#É possível também fazer o desempacotamento de strings
strig = 'ABCD'
print(*strig)

#É possível também fazer o desempacotamento da tupla
tupla = 'Bola', 'cafe', 'maga'
print(*tupla)

salas = [
    ['Maria', 'Helena'], #0
    ['Elaine'],#1
    ['Luiz', 'João', 'Carol', (0, 10, 20, 30, 40)]#2
]

print(*salas , sep= '\n')