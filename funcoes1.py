def exibir_mensagem():
    print("Olá mundo !")


def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome} !')

def exibir_mensagem_3(nome='Anonimo'):
    print(f'Seja bem vindo {nome}')



#exibir_mensagem()
#exibir_mensagem_2(nome='Guilherme')
#exibir_mensagem_3()
#exibir_mensagem_3(nome='Chappie')




#Aprendendo a usar comandos para chamar antecessor e sucessor


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1



    return antecessor, sucessor 


def func_3():
    print('Estamos no Caminho certo não pare !')  
      


#print(calcular_total([10, 20, 34]))
#print(retorna_antecessor_e_sucessor(10))
#print(func_3())   #None (Essa é a palavra que retornou depois da função pré-estabelecida)


#-------------------------------------------//-----------------------------------------------



#Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    #salvar carro no banco de dados.....
    print(f'Carro inserido com sucesso ! {marca}/{modelo}{ano}/{placa}')

#salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')
#salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234')
#salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234'}) 
# os astericos me fala que estou passando um dicionario para aquela função.
#print('Carro inserido com sucesso! Fiat /Palio/ 1999/ ABC-1234)


#-----------------------------------------------//-------------------------------------------------



#Conceitos de args e kwargs:Podemos cobinar parâmetros obrigatórios com args e kwargs.
#Quando esses são definidos(*args e **kwargs),o método recebe os valores com tupla e dicionário respectivamente.

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)
exibir_poema(
    'Sexta-feira, 26 de Agosto de 2022 !',


    'Zen of Python', 'Beautifl is better than ugly.', autor='Tim Peters', ano=1999)  

# na primeira linha e declarada a data/ depois tudo que vier em data e strings entrara no argumento args pois estao separados com virgula e quando eles iram parar os valores separardos por virugulas e entrando valores de chave 
# entra kwargs
      

