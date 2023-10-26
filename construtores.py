class cachorro:
    #init sempre e o contrutor e executado no inicio do processo de instância
    def __init__(self, nome, cor, acordado=True):
        print('inicializandoo a classe....')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
# o del e usado para destruição do objeto usado sempre o final..
    def __del__(self):
        print('Removendo a instância classe.')

    def latido(self):
        print('uau uau')

    def criar_cahorro(self):
        c = cachorro('Bradock', 'Branco', False)
        print(c.nome)   



c = cachorro('chappie', 'amarelo')  
c.latido() 

print('Olá mundo')
del c
print('Olá mundo')
print('Olá mundo')
print('Olá mundo')

