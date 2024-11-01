'''
Acumulador usando função
'''


'''
def soma(*args):#O valor que é 
    #dado para essa função é uma quantidade não numerada
    #Então usamos o empacotamento 
    # o (*args) é uma tupla
    #é  uma Convenção usar *args - Porque são argumentos não nomeados
    
    total = 0 #Acumulador 
    
    for numero in args:
        print('Total', total, numero)
        total= total + numero
        print('Total', total)
    print(total)
    
soma(1,2,3,4,5,6)
'''
def soma(*args):
    total = 0 
    for numero in args:
        total += numero
    return total

    
soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

valor_tupla =1,2,3,4,5,6,7,8,9

#Uma outra maneira de calcular valores  são argumentos não nomeados
print('caluando',sum(valor_tupla))

#Para usar (sum) Tem que estar dentro de uma tupla
print('O sum usa Tupla',type(valor_tupla))

#Mas usando Def soma, Você não pode dar argumentos 
# sendo tupla
# soma(valor_tupla)
#Qual o motivo de dar erro porque ao usar (*args)
#Ele que transforma os valores dados os argumentos dados
#Ao tornarem parâmetros eles se tornam tupla