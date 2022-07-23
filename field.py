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
print('Из файла saves.ini:')
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
print('Из файла players.ini:')
pprint(players)
print()


def show_field(turns) -> None:
    """Вывод псевдографического изображения игрового поля со сделанными ходами"""
    # 🡹 строка документации оформляется не комментарием, а в виде строкового литерала, заключённого в утроенные двойные кавычки
    for key, value in turns.items():
        print(f'Игра: {sorted(tuple(key))}')
        d = dict((k, v) for k, v in value.items())
        dx = d['x']
        del d['x']
        print(f'Игрок {dx} ставит "Х" ')
        print(f'Ходы: {d}')
        d_field = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        # Каждому ходу подставляем соответствующие "Х" и "0"
        for k,v in d.items():
            if k == dx:
                for s in v.replace(',',''):
                    d_field[int(s)] = 'X'
            else:
                for s in v.replace(',',''):
                    d_field[int(s)] = '0'

        print(f'Словарь для подстановки в игровое поле {d_field}')

        # FIXME: почему здесь внезапно появляется плоский range?
        # range для заполнения полей 1-9
        board = range(1,10)
        print('-------------')
        for i in range(3):
            print('|', d_field[board[0+i*3]], '|', d_field[board[1+i*3]], '|', d_field[board[2+i*3]], '|')
            print('-------------')
        print()


show_field(saves)


def check_win(turns) -> None:
    """Логическое значение, есть ли на поле победная комбинация"""
    for key, value in turns.items():
        print(f'Игра: {sorted(tuple(key))}')
        d = dict((k, frozenset(v.replace(',',''))) for k, v in value.items() if k !='x')
        print(d)
        for p,f in d.items():
            if f in ({'1','2','3'}, {'4','5','6'}, {'7','8','9'}, {'1','4','7'}, {'2','5','8'}, {'3','6','9'}, {'1','5','9'}, {'3','5','7'}, {'8','2','3'}):
                print(f'{True})) Победил {p} !!!')
                print()
                break
        else:
            print(f'{False} Нет победной комбинации')


check_win(saves)

