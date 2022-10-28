class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.name = nome
        self.age = idade
        self.eating = comendo
        self.talking = falando

    def falar(self, assunto):
        if self.eating == True:
            print(f'{self.name} não pode falar comendo...')
            return
        elif self.talking == True:
            print(f'{self.name} já está falando...')
            return

        print(f'{self.name} está falando sobre {assunto} :)')
        self.talking = True

    def parar_falar(self):
        if not self.talking == True:
            print(f'{self.name} não está falando')
            return

        print(f'{self.name} parou de falar.')
        self.talking = False

    def comer(self, alimento):
        if self.eating == True:
            print(f'{self.name} já está comendo')
            return
        elif self.talking == True:
            print(f'{self.name} não pode comer falando')
            return

        print(f'{self.name} está comendo {alimento}.')
        self.eating = True

    def parar_comer(self):
        if not self.eating == True:
            print('Não está comendo')
            return

        print(f'{self.name} parou de comer.')
        self.eating = False


p1 = Pessoa('Jamilly', 21)

p1.comer('maça')
p1.parar_comer()
p1.falar('POO')
p1.parar_falar()
p1.comer('Feijão')
