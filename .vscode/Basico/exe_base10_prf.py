#Outro módulo do PY tom
import sys

# expressão regular
# sub (significa substituir)
entrada = input('CPF: ' )
import re
cpf = re.sub(
    r'[^0-9]', '',
    entrada)
#Verificando dados do usuário se não são valores repetidos
entrada_e_sequencial = entrada == entrada[0] *len(entrada)
#replase tira algoo que  não qurtr

#Em casos que o usuário envie dados sequência pode
#fazer uma vez Verificação e fazer ele sair do sistema

if entrada_e_sequencial:
     print("Você enviou dado sequência")
     sys.exit()#Vai executar uma ação que da qual irá fazer usuário sair do sistema



'''
cpf = '746.824.890-70' .replace('.', '')
'''
nove_digitos = cpf[:9]
contador_regressivo =10

resultado =0

for digito in  nove_digitos:
     resultado += int(digito) * contador_regressivo
     contador_regressivo -= 1
digito1 =(resultado * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)

#validação do segundo dígito
des_numero_cpf = nove_digitos + str(digito1)

resultado2 =0
contador_regressivo2 =11
for digito in  des_numero_cpf:
            resultado += int(digito) * contador_regressivo
            contador_regressivo2 -= 1
digito2 =(resultado * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
        
print(digito2)

#fazer a validação do cpf
cpf_gerado_pelo_calculo =  f'{nove_digitos}{digito1}{digito2}'
 
if cpf_gerado_pelo_calculo == cpf_gerado_pelo_calculo:
     print(f'{cpf_gerado_pelo_calculo} é valido')
else:
    print('CPF inválido')