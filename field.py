# FIXME: !!! документируйте модуль !!!
""""""

# TODO и FIXME переводятся как СДЕЛАТЬ и ИСПРАВИТЬ — в этих комментариях я описываю изменения, которых от вас ожидаю; также вы можете аргументировано отстаивать свою версию кода, но уж никак не просто игнорировать мои комментарии

from configparser import ConfigParser as CP
from pprint import pprint


# FIXME: если решили работать в одном модуле, то комментируйте блоки кода
ini1 = 'saves.ini'
ini2 = 'players.ini'

config = CP()
config.read(ini1)

SAVES = {}
for players in config.sections():
    game = frozenset(players.split(','))
    SAVES[game] = dict(config[players])
# FIXME: отсутствует интерпретация полей с данными о ходах
print('Из файла saves.ini:')
pprint(SAVES)
print()

config.clear()
config.read(ini2)

PLAYERS = {}
for player in config.sections():
    PLAYERS[player] = dict(config[player])
# FIXME: два цикла избыточны, можно всё сделать и в одном; переписывайте более эффективный мой код
for into in PLAYERS.values():
    scores = into['stats'].split(',')
    into['stats'] = {'wins': scores[0],
                     'ties': scores[1],
                     'fails': scores[2]}
print('Из файла players.ini:')
pprint(PLAYERS)
print()


def show_field(turns) -> None:
    """Выводит псевдографическое изображение игрового поля со сделанными ходами."""
    for key, value in turns.items():
        print(f'Игра: {sorted(tuple(key))}')
        d = dict((k, v) for k, v in value.items())
        dx = d['x']
        del d['x']
        print(f'Игрок {dx} ставит "Х"')
        print(f'Ходы: {d}')
        d_field = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        # Каждому ходу подставляем соответствующие "Х" и "0"
        for k, v in d.items():
            if k == dx:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'X'
            else:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'O'

        print(f'Словарь для подстановки в игровое поле {d_field}')

        board = range(1,10)
        print('-------------')
        for i in range(3):
            print('|', d_field[board[0+i*3]],
                  '|', d_field[board[1+i*3]],
                  '|', d_field[board[2+i*3]], '|')
            print('-------------')


show_field(SAVES)


def check_win(turns) -> None:
    """Возвращает логическое значение, есть ли на поле победная комбинация."""
    for players, field in turns.items():
        print(f'Игра: {sorted(tuple(players))}')
        players_turns = dict((k, frozenset(v.replace(',','')))
                             for k, v in field.items() if k != 'x')
        print(players_turns)
        for player, f in players_turns.items():
            if f in ({'1','2','3'}, {'4','5','6'}, {'7','8','9'}, {'1','4','7'},
                     {'2','5','8'}, {'3','6','9'}, {'1','5','9'}, {'3','5','7'}):
                print(f'{True} Победил {player} !!!\n')
                break
        else:
            print(f'{False} Нет победной комбинации ...\n')


check_win(SAVES)

