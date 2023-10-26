class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor


#o def e usada para definir uma função e assim que usar definir um argumento

    def buzinar(self):
        print('plim plim')

    def parar(self):
         print('parando bicicleta .....')
         print('bicicleta parada')

    def correr(self):
        print('vrum') 

   # def __str__(self):
        #return f'bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor-{self.valor}.'    

    def __Str__(self):
        return f'{self.__class__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
    
b1 = bicicleta ("vermelha", 'valor', 2023, 600)
b1.buzinar()
#b1.correr()
#b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


#b2 = bicicleta('verde', 'monark', 2000, 500)
#b2.buzinar() #bicicleta.buzinar(b2)
#print(b2.cor)
