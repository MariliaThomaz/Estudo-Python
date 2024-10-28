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

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de  {multiplo}, end =' ' ')
    print(resultado)

multiplo_de(16,8)
multiplo_de(15,3)
multiplo_de(10,2)