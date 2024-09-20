#Introdução ao desempacotamento 

nomes = ['Pedro','Giovana','Catarina']

nome1, nome2,  nome3 = nomes

print(nome2)

#pode ser feito Outra maneira

nome4, nome5, nome5 = ['bia', 'leonardo', 'Júlia']

print(nome4)

#Imaginando tendo uma lista de dados muito grande
#Mas você gostaria de pegar apenas um item da lista
#Mas você ao escolher o item que gostaria de obter
#Você tem Dar um destino ao restante dos dados que você não quer

_, nome, *_ = ['bia', 'leonardo', 'Júlia']

print(nome)

print(f'restante da lista: {_}')

#Tem uma boa ética de programação fazer variáveis que da qual
#Você não usará futuramente ou executar algo com ela não é uma boa prática
#E uma boa cultura é colocar um underline nela
#Usar o underline não significa que não é uma variável mas é 
# uma prática de programação para identificar pra 
# outros programadores que esse dado que está
#sendo colocado ali não é um valor que será utilizado durante o código