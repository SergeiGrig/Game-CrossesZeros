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
    """функция вывода псевдографического изображения игрового поля со сделанными ходами"""
    # 🡹 строка документации оформляется не комментарием, а в виде строкового литерала, заключённого в утроенные двойные кавычки
    for el in turns:
        pass
    board = range(1,10)
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')
    for el in turns:
        print(turns[el])
    # print()

show_field(saves)
