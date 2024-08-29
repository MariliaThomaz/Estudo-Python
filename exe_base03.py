#Desenvolvendo uma calculadora simples usando laço de repetição
#
while True:
    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')
    #Tratamento para filtragem de dados do input
  
    #sair = sair.lower() Estou pegando um método que faz ação de pegar respopta da saída e transformar sua resposta em letras minúsculas
   
    #Devido ao pyton ser uma linguagem que ele vê tudo por objeto 
    # vamos usar um método.

    #A procura da praticidade podemos usar outro método 
    # pegando apenas a primeiro índice da resposta.
    # sair = sair.startswith('s')
 
      
    print(sair)