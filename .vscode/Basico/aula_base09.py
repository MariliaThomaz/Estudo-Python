#imprecisão dos pontos flutuantes


numero_1 = 0.1
numero_2 = 0.7
 
soma = numero_1 + numero_2

print(soma)
#0.7999999999999999 este  valo é  um  valor  impreciso

print(f'Formação F: {soma:.2f}')

#esse problema de trabalhar com pontos flutuantes números imprecisos
#não se encontra somente na linguagem PY
#podemos ver que há uma documentação sobre
#Double-precisio floating-point  format IEEE 754

# a várias formas de manipular, a questão de pontos flutuantes

# --> (1)
#esta maneira, é uma das possibilidades de formatar o resultado.
#nesse exemplo abaixo é esta sendo modificado o resultado final
print(type(f'Formação F: {soma:.2f}'))

# --->(2)
#existe uma função em PY chamado  ROUND
#para usar essa função você vai indica variável que deseja usar a função
#variável que deseja usar a função quantas casas decimal você deseja
#usar esta essa função a variável ainda continua sendo floyd
print('Round')
print(type(round(soma,2)))


#--> (3)
#módulo em python de usar o decimal
#e se decimal tem um modulo uma  classe interna 
#mas qual é a necessidade de fazer uma conta com tantas casas decimais
#tudo depende da seu tudo depende da sua necessidade
#tá da necessidade de ter essas informações PY te proporciona
# uma biblioteca da qual tem um módulo que ela cansa os milésimos
import decimal
numero_x1 = decimal.Decimal(0.4)
numero_x2 = decimal.Decimal(0.8)
soma_d = numero_x1 + numero_x2
print(f'Soma usnado Decimal: {soma_d}')