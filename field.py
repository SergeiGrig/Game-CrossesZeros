from configparser import ConfigParser as CP
from pprint import pprint

ini1 = 'saves.ini'
ini2 = 'players.ini'

config = CP()
config.read(ini1)

saves = {}
for players in config.sections():
    game = frozenset(players.split(','))
    saves[game] = dict(config[players])
pprint(saves)
print()

config.clear()
config.read(ini2)

players = {}
for player in config.sections():
    players[player] = dict(config[player])
for into in players.values():
    scores = into['stats'].split(',')
    into['stats'] = {'wins': scores[0],
                     'ties': scores[1],
                     'fails': scores[2]}
pprint(players)
print()


def show_field(turns) -> None:
    # функция вывода псевдографического изображения игрового поля со сделанными ходами
    for key,value in turns.items():
        print(f'{key=} {value=}')
        for key,valueN in value.items():
            board = range(1,10)
            tuple(valueN[board[0]])
            print('-------------')
            for i in range(3):
                print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
                print('-------------')
            # for els in turns:
            #     print(turns[els])
        # print()
show_field(saves)