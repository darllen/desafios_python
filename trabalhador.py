""" 
Crie um programa que leia nome, o ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quandos anos a pessoa vai se aposentar.
"""

people = {}

people['name'] = input('Nome: ')
born = int(input('Ano de Nascimento: '))
people['age'] = 2022 - born
people['ctps'] = int(input('Carteira de Trabalho: '))

if people['ctps'] != 0:
    people['hire'] = int(input('Ano de contratação: '))
    people['wage'] = float(input('Salário: R$ '))
    people['retire'] = (people['hire'] + 35) - born

print('-='*10)
for e in people:
    print(f'{e} tem valor {people[e]}')
