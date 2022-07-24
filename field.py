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


# TODO: внесите все необходимые правки, уберите лишнее из этой функции — и я покажу вам альтернативную версию функции вывода поля для вашей структуры данных
def show_field(turns) -> None:
    """Выводит псевдографическое изображение игрового поля со сделанными ходами."""
    # FIXME: и зачем здесь перебирать все СОХРАНЁННЫЕ партии?
    for key, value in turns.items():
        # FIXME: для того, чтобы отсортировать frozenset, не нужно его преобразовывать в кортеж
        print(f'Игра: {sorted(tuple(key))}')
        # FIXME: а ещё можно использовать функцию deepcopy из модуля copy
        d = dict((k, v) for k, v in value.items())
        # FIXME: две строки кода ниже заменяются одной: dx = d.pop('x') — прочитайте в документации, что это за словарный метод
        dx = d['x']
        del d['x']
        # Игрок player1 ставит "Х" — составляйте, пожалуйста, менее двусмысленные фразы; я целую минуту пытался понять, где и зачем вы тут устроили моделирование игрового процесса
        print(f'Игрок {dx} играет крестиком')
        print(f'Ходы: {d}')
        # FIXME: есть такой словарный метод fromkeys() — очень подходит в текущей ситуации — мы его разбирали на занятии (dict7.py), и, конечно, он есть в документации
        d_field = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        # Каждому ходу подставляем соответствующие "Х" и "O"
        for k, v in d.items():
            if k == dx:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'X'
            else:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'O'

        print(f'Словарь для подстановки в игровое поле {d_field}')

        # TODO: в текущих обстоятельствах такой код безусловно работает — но только в текущих — наступит момент, когда он работать перестанет, и вам нужно будет его переписывать =)
        #       пока я сохраняю интригу, вам стоит попробовать вообразить эту(-и) ситуацию(-и) — это в любом случае нужно делать всегда: стараться представить все ситуации, в которых окажется любой ваш код
        board = range(1,10)
        print('-------------')
        for i in range(3):
            print('|', d_field[board[0+i*3]],
                  '|', d_field[board[1+i*3]],
                  '|', d_field[board[2+i*3]], '|')
            print('-------------')

# TODO: очень важно для каждого проекта осмыслить управление переменными в разных областях видимости с учётом передачи по ссылке и по значению:
#  1. какие переменные будут глобальными, какие локальными
#  2. в каких случаях необходимо передавать переменные (или их копии), а в каких работать с глобальными из локальной области видимости
#  3. на каких этапах вы будете создавать копии тех глобальных переменных, которые необходимо передавать по ссылке

# FIXME: опишите сценарий, в котором потребуется одним вызовом функции вывести игровые поля из всех СОХРАНЁННЫХ партий
show_field(SAVES)
# TODO: если вы используете сохранённые партии для тестов, то вам нужно написать соответствующий код вне функции — в которую вы передаёте одну партию — именно в таком режиме и должна работать эта функция, что и написано у вас в документации к этой функции


def check_win(turns) -> None:
    """Возвращает логическое значение, есть ли на поле победная комбинация."""
    # FIXME: и зачем здесь перебирать все СОХРАНЁННЫЕ партии?
    for players, field in turns.items():
        # FIXME: 1. для того, чтобы отсортировать frozenset, не нужно его преобразовывать в кортеж
        #        2. зачем здесь вообще сортировка по алфавиту?
        #           может, лучше вывести по порядку: игрок-крестик, игрок-нолик?
        print(f'Игра: {sorted(tuple(players))}')
        players_turns = dict((k, frozenset(v.replace(',','')))
                             for k, v in field.items() if k != 'x')
        print(players_turns)
        for player, f in players_turns.items():
            # FIXME: неа, так не работает — что если у игрока больше трёх символов на поле? добавил в saves.ini соответствующий тестовый вариант
            if f in ({'1','2','3'}, {'4','5','6'}, {'7','8','9'}, {'1','4','7'},
                     {'2','5','8'}, {'3','6','9'}, {'1','5','9'}, {'3','5','7'}):
                print(f'{True} Победил {player} !!!\n')
                break
        else:
            print(f'{False} Нет победной комбинации ...\n')

# FIXME: опишите сценарий, в котором потребуется одним вызовом функции проверить на победные комбинации все СОХРАНЁННЫЕ партии
check_win(SAVES)
# TODO: если вы используете сохранённые партии для тестов, то вам нужно написать соответствующий код вне функции — в которую вы передаёте одну партию — именно в таком режиме и должна работать эта функция, что и написано у вас в документации к этой функции
