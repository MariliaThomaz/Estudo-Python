#Desenvolvendo uma calculadora simples usando laço de repetição
#

numero1_covite_flo =0.0
numero2_covite_flo =0.0
numero2_covite_int =0
numero1_covite_int =0
while True:
    nf2=0
    nf1=0
 
    print('Ola esta  na Calciladora.')
    
    numero1 = input('Digite o primero nuemro =')

    if '.' in numero1:
        numero1_covite_flo = float(numero1)
        
        nf1 =+1
    
    else:
        numero1_covite_int = int(numero1)

    numero2 = input('Digite o segundo nuemro =')

    if '.' in numero2:

        numero2_covite_flo = float(numero2)
        nf2 =+1
    else:
        numero2_covite_int = int(numero2)
    


    operador = input('Infome qual operador matetido: +, - , / ou * ')

    if operador == '+':
        if nf1 == 1 and ( nf2 ==1): 
             somaflot = numero1_covite_flo + numero2_covite_flo
             print(f'Soma float; {somaflot}')

        elif nf1 == 0  and  nf2 == 1:
            soma_I_f = numero1_covite_int + numero1_covite_flo
            print(f'Soma: {soma_I_f=}')
          
        elif nf1 == 1 and  nf2 == 0:
            soma_F_I = numero1_covite_flo + numero1_covite_int
            print(F'Soma: {soma_F_I=}')
            
        elif nf1 == 0 and  nf2 ==  0:
          somaint = numero1_covite_int + numero2_covite_int
          print(f'Soma int; {somaint}')

    elif operador == '-':
         
        if nf1 == 1 and ( nf2 ==1): 
             negF_F =  numero1_covite_flo - numero2_covite_flo
             print(f'Subritração: {negF_F=}')

        elif nf1 == 0  and  nf2 == 1:
            negaI_F = numero1_covite_int - numero1_covite_flo
            print(f'Subritração {negaI_F=}')
          
        elif nf1 == 1 and  nf2 == 0:
           nega_F_I = numero1_covite_flo - numero1_covite_int
           print(F'Subritração {nega_F_I=}')
        
        elif nf1 == 0 and  nf2 ==  0:
          negaI_I = numero1_covite_int - numero2_covite_int
          print(f'Subritração {negaI_I=}')

    elif operador == '/':
         
        if nf1 == 1 and ( nf2 ==1): 
             divF_F =  numero1_covite_flo / numero2_covite_flo
             print(f'Divisão: {divF_F=}')

        elif nf1 == 0  and  nf2 == 1:
            divI_F = numero1_covite_int / numero1_covite_flo
            print(f'Divisão: {divI_F=}')
          
        elif nf1 == 1 and  nf2 == 0:
           div_F_I = numero1_covite_flo / numero1_covite_int
           print(F'Divisão {div_F_I=}')
        
        elif nf1 == 0 and  nf2 ==  0:
          divI_I = numero1_covite_int / numero2_covite_int
          print(f'Divisão {divI_I=}')

    elif operador == '*':
         
        if nf1 == 1 and ( nf2 ==1): 
             vesF_F =  numero1_covite_flo * numero2_covite_flo
             print(f'Multiplicação: {vesF_F=}')

        elif nf1 == 0  and  nf2 == 1:
            vesI_F = numero1_covite_int * numero1_covite_flo
            print(f'Multiplicação {vesI_F=}')
          
        elif nf1 == 1 and  nf2 == 0:
           ves_F_I = numero1_covite_flo * numero1_covite_int
           print(F'Multiplicação {ves_F_I=}')
        
        elif nf1 == 0 and  nf2 ==  0:
          vesI_I = numero1_covite_int * numero2_covite_int
          print(f'Multiplicação {vesI_I=}')


    
  




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
      
