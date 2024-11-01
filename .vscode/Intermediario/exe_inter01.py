# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    
 
  
    primero = args[0]
    print(primero)
    total = primero 

    for numero in args:
        
         total *= numero
         print(total,numero)
    print(total)
    
multiplica(1,2,3,4,5,6)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def impa_par (valor):
    
     multiplo_de_dois = valor % 2 == 0
     
     if multiplo_de_dois:
        return f'{valor} é par'
     return f'{valor} é ímpar'

print(impa_par(21))
print(impa_par(20))