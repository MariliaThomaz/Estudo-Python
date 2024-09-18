'''
Faça um jogo para o usuário digitar qual a palavra secreta 
você vai procurar a palavra secreta qual vai dar a possibilidade para o 
usuário digitar apenas uma letra quando o usuário digitar
 uma letra você vai conferir se a letra digitada está na palavra 
 secreta se a letra digitada escrita na palavra secreta exiba a letra se 
 a letra digitada não SKU tiver na palavra secreta exiba* faça a 
 contagem tentativa do usuário
'''
#modo para esecutar comando 
import os

palavachave = 'refriado'
letras_acetadas =''
numero_tentativa = 0
while True:

    letra = input('Digite uma letra da palavra secreta: ')
    quantidade = len(letra)
    numero_tentativa +=1

    if quantidade > 1:
           print("Você só pode digitar uma letra por vez.")
    if letra == ' ' :
         print("Não pode haver espaço em branco.")
         continue
    
    if letra in palavachave:
        letras_acetadas += letra

    palavra_formada = ''

#Estou percorrendo letra letra da palavra
    for i in palavachave:
        if i in letras_acetadas:
          palavra_formada += i
     
        else:
            palavra_formada += '*'
    
    print('Palavra formada',palavra_formada)

    if palavra_formada == palavachave:
        os.system('cls')# ele limpa  o  terminal
        print(" Ganhou !!! Parabens !!!!")
        print('A PALAVRAS ERA: ', palavachave)
        print('Numero de tentativas: ', numero_tentativa)

        letras_acetadas = '' #reseta  jogo
        numero_tentativa =0


         
        
         



