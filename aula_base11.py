#Lista dentro de lista

salas = [
    ['Maria', 'Helena'], #0
    ['Elaine'],#1
    ['Luiz', 'João', 'Carol', (0, 10, 20, 30, 40)]#2
]

print(f'vendo  todas  listas {salas}')
print(f'vendo  lista 2 o dado 2: {salas[2][1]}')
print(f'vendo  lista 2 o dado que esta tupla : {salas[2][3][2]}')