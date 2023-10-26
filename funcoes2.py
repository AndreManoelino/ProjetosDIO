#Parâmetros especias por posição ou nome:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro('Palio',1999, 'ABC-1234', marca='fiat', motor='1.0',combustivel='Gasolina' ) #válido
#criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='fiat', motor='1.0', combustivel='Gasolina') #inválido    



#---------------------------------------------------/////---------------------------------------------


#keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='fiat', motor='1.0', combustivel='gasolina') #válido

#criar_carro('Palio', 1999, 'ABC-1234', marca='fiat', motor='1.0', combustivel='Gasolina') #inválido

#---------------------------------------///-----------------------------------------------

# keyword and positional only
# Esse comando chama para mostrar os primeiros valores por posição enquanto os outros são chamados pelo padrão nome
def criar_carro( modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro('Palio', 1999, 'ABC-1234', marca='fiat', motor='1.0', combustivel='gasolina') #válido

#criar_carro('Palio', 1999, 'ABC-1234', marca='fiat', motor='1.0', combustivel='Gasolina') #inválido


#--------------------------------------------///-------------------------------------
# Objetos de primeira classe:funções são objetos,(listas,tuplas,dicionários,etc)
def somar(a, b):
    return a + b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

#exibir_resultado(10, 10, somar)    # o resultado da operação 10 + 10 = 20


#-----------------------------------------------////-------------------------------------

#Escopo local e escopo global essa e uma prática e deve ser evitada.
#Exemplo:

salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'lista aux={lista_aux}')

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)




C = int(input())

for i in range(C):
    N = int(input())
    if N <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")


