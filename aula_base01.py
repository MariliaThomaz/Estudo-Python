

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