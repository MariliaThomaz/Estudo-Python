"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
sair = ' '
while True:
  

    usario_cpf = input ("Digite as CPF: ")
    cotaguem_cpf=len(usario_cpf)
    if usario_cpf in ' ':
        print("desculp e você não digitou nada")
        continue
    elif cotaguem_cpf > 14:
        print("Seu CPF escrito errado")
        continue
    elif cotaguem_cpf < 14:
        print("Seu CPF incompleto")
        continue
    else:
        strig_cpf = usario_cpf.replace('.', '').replace('-', '')
        
        despaconta = list(strig_cpf)
        nove_numero_cpf =(despaconta[:9])
        
        #10

        des= int(nove_numero_cpf[0])
        vese_des= des * 10 
        print(f'10x{des}= {vese_des}')
        
        #9
        nove= int(nove_numero_cpf[1])
        vese_nove= nove * 9 
        print(f'9x{nove}= {vese_nove}')
        
        #8
        oito= int(nove_numero_cpf[2])
        vese_oito= oito * 8
        print(f'8x{oito}= {vese_oito}')
        
        #7
        sete= int(nove_numero_cpf[3])
        vese_sete= sete * 7
        print(f'7x{sete}= {vese_sete}')
        
        #6
        seis= int(nove_numero_cpf[4])
        vese_seis= seis * 6
        print(f'6x{sete}= {vese_seis}')
        
        #5
        cinco= int(nove_numero_cpf[5])
        vese_cinco= cinco * 5
        print(f'5x{cinco}= {vese_cinco}')
        
        #4
        quatro= int(nove_numero_cpf[6])
        vese_quatro= quatro * 4
        print(f'4x{quatro}= {vese_quatro}')
        
        #3
        tres= int(nove_numero_cpf[7])
        vese_tres= tres * 3
        print(f'3x{tres}= {vese_tres}')
        
        #2
        dois= int(nove_numero_cpf[8])
        vese_dois= dois * 2
        print(f'2x{dois}= {vese_dois}')

    somatodos_v =vese_des+ vese_nove+ vese_oito+ vese_sete+ vese_seis+ vese_cinco+vese_quatro+ vese_tres+vese_dois
    print(f'Soma: {somatodos_v}')
    
    #Multiplicar o resultado anterior por 10
    mutiplica = somatodos_v * 10
    print(f'Multiplicação do resutado 10: {mutiplica}')
    #Obter o resto da divisão da conta anterior por 11
    resto = mutiplica % 11
    print(f'Resto: {resto}')
    #Se o resultado anterior for maior que 9:
    if resto > 9:
        print(f'restado 0')
    else:
         print(f'resultado é o valor da conta')
  
  #fazendo validação do segundo número do cpf    
    des_numero_cpf =(despaconta[:10])   
    contador_regressivo =11

    resultado =0

    for digito in  des_numero_cpf:
            resultado += int(digito) * contador_regressivo
            contador_regressivo -= 1
    digito1 =(resultado * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0
        
    print(digito1)

   
  
