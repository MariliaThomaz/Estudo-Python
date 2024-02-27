"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_int = input('Digite o número: ')


try: 
    nume_comv = int(numero_int)
    restante = nume_comv % 2
    if restante == 1:
        print(f'Este valor  é impar: {nume_comv}')
    else:
        print(f'Este valor  é par: {nume_comv}')
except:
    print('Valor digitado inválido')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Me informe que horas são: ')
horas_c = float(horas)


if 0.00 <= horas_c < 12.00:
    print("Bom dia")
elif 12.00 <= horas_c < 18.00:
    print("Boa tarde")
elif 18.00 <= horas_c <= 23.59:
    print("Boa noite")
else:
    print("Hora inválida")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
quantida_nome = len(nome)
if quantida_nome <= 4:
    print('Seu nome é curto')
elif  5 >= quantida_nome  <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")