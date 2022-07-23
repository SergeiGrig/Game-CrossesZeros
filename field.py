# FIXME: !документируйте модуль!
""""""

# TODO и FIXME переводятся как СДЕЛАТЬ и ИСПРАВИТЬ — в этих комментариях я описываю изменения, которых от вас ожидаю; также вы можете аргументировано отстаивать свою версию кода, но уж никак не просто игнорировать мои комментарии

from configparser import ConfigParser as CP
from pprint import pprint


# FIXME: если решили работать в одном модуле, то комментируйте блоки кода
ini1 = 'saves.ini'
ini2 = 'players.ini'

config = CP()
config.read(ini1)

saves = {}
for players in config.sections():
    game = frozenset(players.split(','))
    saves[game] = dict(config[players])
    # FIXME: отсутствует интерпретация полей с данными о ходах
pprint(saves)
print()

config.clear()
config.read(ini2)

players = {}
for player in config.sections():
    players[player] = dict(config[player])
# FIXME: два цикла избыточны, можно всё сделать и в одном; переписывайте более эффективный мой код
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
    for key, value in turns.items():
        print(f'Игра: {sorted(tuple(key))}')
        print(f'Ходы: {dict((k,v) for k,v in value.items())}')
        a = turns[frozenset({'player1', 'player2'})]['x']
        print(a)

        for key, valueN in value.items():
            # FIXME: почему здесь внезапно появляется плоский range?
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