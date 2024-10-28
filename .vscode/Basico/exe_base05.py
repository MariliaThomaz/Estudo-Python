frase = 'aaaooo'

i =0

qtd_apareceu_mais_vezes =0 
letra_apareceu_mais_veze = ''

while i < len(frase):
    letra_atual = frase[i]

    if  letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_veze = letra_atual
    i += 1


print(
        ' A Letra que aparece mais vezes foi'
        f' {letra_apareceu_mais_veze} que apareceu'
        f' {qtd_apareceu_mais_vezes} x'

    )

