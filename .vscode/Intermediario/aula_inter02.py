'''
o escopo de uma função em pyton
escopo significa o local aonde aquele código pode atingir.
existem o escopo global e local
o escopo global é o escopo aonde todo o código é alcançável
o escopo local é o escopo aonde apenas o nome do mesmo local
podem ser alcançados
'''

x =1 #modulo

def escopo():
    x =10#escopo escopo()
    def outro_funcao():
        y = 2#escopo outro_funcao()
        print(x,y)
        
    outro_funcao()
    print(x)
    
print(x)
escopo()
print(x)