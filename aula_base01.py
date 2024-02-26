

print('Hello World !')

"""
É um tipo de comentário para usar em casos de textos grandes porém o interpretador do PY
  faz a lê ao contrário do cerquilha
  DocString
  """

'''
O python = linguagem de programação
O tipo de tipagem dinâmica / forte

'''

#Dizer dinâmica é que ele já sabe a tipagem da valor da do para ele

#T caracter de escape
print("Marilia \"Thomaz\"")

#CRLF é  modo  que os  printes  acontece  ele  pula  a  linha

#numos inteiros
print(11)
print(-11)
print('0',type(0))

#flout
print(1.1)

#covetendo o tipo  

resebe = 5

print("o tipo da varivel é: ", resebe, type(resebe))

print("o covetendo o valor 5: ",  type(str(resebe)))

valor1 = 10
valor2 = 3
# divisão normal
print('divisão que não corta as casas decimais::', valor1 / valor2  ) #ela sempre retorna um valor de ponto flutuante independente do valor

print('reduce arredonda as casas de se', valor1 // valor2  )

#precedência de matemática
#interpretador do código qual é a ordem que o pY calcula os dados
 # 1 (N+ N)
 # 2 **
 # 3 * / // %
 # 4 + - 

print("***********calculo do IMC*************")
nome = 'Marilia'
altura =   1.67
peso = 53.5
imc = peso / (altura * altura)

print(nome ,'tem', altura)
print('peso', peso, 'quilo e seu IMC É: ')
print(imc)

# fomartação de texto para exibir
# qunapd ver - > f <-  é  significa que a formatação o seu nome é "f-strings"
print(f'{nome} tem {altura} o seu peso é: {peso} seu IMC {imc:.2f}')

#Tudo em pyton é objeto, O porquê porque todos os objetos têm métodos dentro dele
#E o que característica de um objeto todo objeto tem ações que são métodos coisas que ele pode fazer
#Usando uma função para mudar o objeto

a = 'A'
b = 'B'
c = 8.999
# Isso é um método -> .format()
fomando =  'a={} b={} c={:.2f}'.format(a,b,c)
print(f'formatando usando um metodo: {fomando}')

#Parâmetro nomeado
m = 'M'
v = 'V'
t = 4.012350
# Isso é um método -> .format()
strig = 'm={nome1} v={nome2} t={nome3}'
fomatando = strig.format(nome1=m,nome2=v,nome3=t)
print(fomatando)

#Input é como coletar dados do usuário
#input é uma  função 

""" input('Qual é seu nome: ')"""

#Para coletar os dados do input tem que sempre lembrar que é retornado no tipo d string
#Devido ela ser do tipo de string você tem que fazer a conversão no caso de precisar, Tipos numéricos

nome = input('Qual é seu nome: ')

idade1 = int(input('Qual é a sua idade: '))
autura = input('Qual é a sua altura: ')
print(f'O nome  é: {nome}, idade: {idade1}, altura:  {altura}')

capirue_altura_convete_float = float(autura)
somando = idade1 + capirue_altura_convete_float

print(f'Soma da altura: {capirue_altura_convete_float} + {idade1} idade = {somando}')