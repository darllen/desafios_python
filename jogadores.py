""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, 
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
Aprimore a questão para que ele funciona com vários jogadores, incluindo um sistema de 
visualização de detalhes do aproveitamento de cada jogador.
"""
jogadores = []

ask = 'S'

while ask == 'S':
    jogador, gols = {}, []
    name = input('Nome do Jogador: ')
    matches = int(input(f'Quantas partidas {name} jogou? '))
    [gols.append(int(input(f'Quantos gols na partida {p}? '))) for p in range(
        1, matches+1)]

    jogador['name'] = name
    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador)

    ask = input('Deseja continuar? [S/N] ').upper()
    if ask == 'N':
        break

print('-='*40)
print('cod   nome      gols        total')
print('-'*30)
opt = {}
for i in range(len(jogadores)):
    nome, q_gols, t_gols = jogadores[i]['name'], jogadores[i]['gols'], jogadores[i]['total']
    print(f'{i+1}   {nome}   {q_gols}        {t_gols}')
    opt[i+1] = jogadores[i]

print('-'*30)
ask = 0
while ask != 999:

    choice = int(input('Mostrar dados de qual jogador? '))
    if choice != 999:
        aaa = opt[choice]['name']
    print(f'-- LEVANTAMENTO DO JOGADOR {aaa}: ')


for i in range(len(gols)):
    dic = jogadores[i]
    ccc = dic['gols']
    for e in ccc:
        print(f'No jogo {i} fez {e} gols.')


print('-'*30)
ask = choice

print(jogadores)
