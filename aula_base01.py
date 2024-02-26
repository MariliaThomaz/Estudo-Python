

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

#Operadores condicionais
entrada = input('Você quer entrar ou sair? ')
if entrada == 'entrda' or   entrada == 'e':
    print('Continue')
#elif = se não se
#Observando o elite você consegue fazer condições 
#Em vez de você usar um novo i fi você usa ele Elif
elif entrada == 'sair' or   entrada == 's':
    print('saida')
else:
    print("Você digitou nenhuma das alternativas")

#**************** vendo qual é valo menor
primo_n = input('Digite o primeiro número: ')
cegundo_n =input('Digite o segundo número: ')

if(primo_n > cegundo_n):
    print(f' o Primeiro número é maior {primo_n}')
elif(primo_n == cegundo_n):
    print('Os 2 números são iguais')
else:
     print(f'o Segundo número é maior {cegundo_n}')

     #Avaliação de curto circuito
     print(True and 0 and True)

     #Avaliação de curto circuito
     print(True or 0 or True)

     #operadore in not  in
    #strings são interáveis
    #Isto quer dizer que eu posso pegar caracter por caracter através do Python
    
pega = 'julia é  muito bonita'

print(pega[3])

#pega um valo
print('é' in pega)
print('v' in  pega)

print('********************************************************')

#Interpolação 
#Interpolação de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal 

nome2 = 'Patrica'
preco = 50000000.4050
esibe1 = '%s, o preço é R$:.2%f ' % (nome2,preco)
print (esibe1)

#Hexadecimal
print('o hexadecimal de %d é %08X' % (1500,1500))

# Fatiamento de strings
fatiamento = 'Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference.'

# fatimento [i:f:p] [::]
print(fatiamento[4:8])
print(fatiamento[8:])

# Ele conta a quantidade de caracteres
print(len(fatiamento))

# fatimento [i:f:p] 
# i = indees 
# f parada
# p é  numeop de  Passos  É a quantidade de pulo que vai dar
print(fatiamento[4:8:3])

#Invertendo nome através do fatiamento
print(f'Invertendo o nome através do fatiamento: {nome[::-1]}')

#tratamento de exeção  -> try/execept
#Tratamto de erro
teste_num = input('Digite um número: ')

try:
    print('Exibindo o que foi digitado:', teste_num)
    convet_floar = float(teste_num)
    print(f'O dobro do número digitado{convet_floar} é {teste_num *2}')
except:
    print('Isso não é um número')m