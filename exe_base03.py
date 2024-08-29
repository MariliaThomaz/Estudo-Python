#Desenvolvendo uma calculadora simples usando laço de repetição
#
while True:

    print('Ola esta  na Calciladora.')

    numero1 = input('Digite o primero nuemro =')
    numero1_covite_int = int(numero1)
    numero1_covite_flo = float(numero1)


    numero2 = input('Digite o segundo nuemro =')
    numero2_covite_int = int(numero2)
    numero2_covite_flo = float(numero2)

    

    operador = input('Infome qual operador matetido: +, - , / ou * ')

    if operador == '+':
        somaint = numero1_covite_int + numero2_covite_int
        print(f'Soma int; {somaint}')

    elif  operador == '+':
        somaflot = numero1_covite_flo + numero2_covite_flo
        print(f'Soma float; {somaflot}')


       
    
     




  
    




    #################################################################
    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')
    #Tratamento para filtragem de dados do input
  
    #sair = sair.lower() Estou pegando um método que faz ação de pegar respopta da saída e transformar sua resposta em letras minúsculas
   
    #Devido ao pyton ser uma linguagem que ele vê tudo por objeto 
    # vamos usar um método.

    #A procura da praticidade podemos usar outro método 
    # pegando apenas a primeiro índice da resposta.
    # sair = sair.startswith('s')
    
    if sair is True:
        break
      
