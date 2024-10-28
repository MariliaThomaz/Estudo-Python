#Cuidado com os dados mutáveis

lista_a = ['Faustino', 'Bri Zelda']
print(f'Lista A: {lista_a}')
#Pode também usar um método de copiar
'''lista_b =lista_a.copy()'''
#Mas usando esse método é ele deixa as listas separada
lista_b = lista_a
print(f'Lista B: {lista_b}')

#O cuidado tem que ser visto após se eu quiser acrescentar algum dado
#A lista_a Ele automaticamente muda a lista_b pois vemos que acima
#Que a lista_b recebeu alista_a

lista_a.append('São canarinhos amarelos')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
