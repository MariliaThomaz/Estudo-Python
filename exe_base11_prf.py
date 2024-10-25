#Gerar novos CPF

#Módulo Random Ele gera informações aleatórias 
import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

print(nove_digitos)

contador_regressivo =10

resultado =0

for digito in  nove_digitos:
     resultado += int(digito) * contador_regressivo
     contador_regressivo -= 1
digito1 =(resultado * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0


#validação do segundo dígito
des_numero_cpf = nove_digitos + str(digito1)

resultado2 =0
contador_regressivo2 =11
for digito in  des_numero_cpf:
            resultado += int(digito) * contador_regressivo
            contador_regressivo2 -= 1
digito2 =(resultado * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
        


#fazer a validação do cpf
cpf_gerado_pelo_calculo =  f'{nove_digitos}{digito1}{digito2}'
print(cpf_gerado_pelo_calculo)
 