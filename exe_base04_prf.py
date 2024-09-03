
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - * /): ')

    num_1_float = 0
    num_2_float = 0

    numeros_validos = None

    try: 
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print('Um dos números digitados não são válidos')
            continue
    operador_pemitidos = '+-/*'
    if operador not in operador_pemitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    print('Realizando sua conta. Confira o seu resultado abaixo: ')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
     print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui. ')




    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break