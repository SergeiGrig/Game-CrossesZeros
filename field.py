# ДОБАВИТЬ: !!! документируйте модуль !!!
""""""

from configparser import ConfigParser as CP
from pprint import pprint


# ДОБАВИТЬ: если решили работать в одном модуле, то комментируйте блоки кода
ini1 = 'saves.ini'
ini2 = 'players.ini'

config = CP()
config.read(ini1)

SAVES = {}
for players in config.sections():
    game = frozenset(players.split(','))
    SAVES[game] = dict(config[players])
# ДОБАВИТЬ: отсутствует интерпретация полей с данными о ходах
print('Из файла saves.ini:')
pprint(SAVES)
print()

config.clear()
config.read(ini2)

PLAYERS = {}
for player in config.sections():
    PLAYERS[player] = dict(config[player])
# ИСПРАВИТЬ: два цикла избыточны, можно всё сделать и в одном; переписывайте более эффективный мой код
for into in PLAYERS.values():
    scores = into['stats'].split(',')
    into['stats'] = {'wins': scores[0],
                     'ties': scores[1],
                     'fails': scores[2]}
print('Из файла players.ini:')
pprint(PLAYERS)
print()


# СДЕЛАТЬ: внесите все необходимые правки, уберите лишнее из этой функции — и я покажу вам альтернативную версию функции вывода поля для вашей структуры данных
def show_field(turns) -> None:
    """Выводит псевдографическое изображение игрового поля со сделанными ходами."""
    # ИСПРАВИТЬ: и зачем здесь перебирать все СОХРАНЁННЫЕ партии?
    for key, value in turns.items():
        # ИСПРАВИТЬ: для того, чтобы отсортировать frozenset, не нужно его преобразовывать в кортеж
        print(f'Игра: {sorted(tuple(key))}')
        # ИСПРАВИТЬ: а ещё можно использовать функцию deepcopy из модуля copy
        d = dict((k, v) for k, v in value.items())
        # ИСПРАВИТЬ: две строки кода ниже заменяются одной: dx = d.pop('x') — прочитайте в документации, что это за словарный метод
        dx = d['x']
        del d['x']
        # Игрок player1 ставит "Х" — составляйте, пожалуйста, менее двусмысленные фразы; я целую минуту пытался понять, где и зачем вы тут устроили моделирование игрового процесса
        print(f'Игрок {dx} играет крестиком')
        print(f'Ходы: {d}')
        d_field = dict.fromkeys({1, 2, 3, 4, 5, 6, 7, 8, 9}, " ")
        # Каждому ходу подставляем соответствующие "Х" и "O"
        for k, v in d.items():
            if k == dx:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'X'
            else:
                for s in v.replace(',', ''):
                    d_field[int(s)] = 'O'

        print(f'Словарь для подстановки в игровое поле {d_field}')

        # СДЕЛАТЬ: в текущих обстоятельствах такой код безусловно работает — но только в текущих — наступит момент, когда он работать перестанет, и вам нужно будет его переписывать =)
        #       пока я сохраняю интригу, вам стоит попробовать вообразить эту(-и) ситуацию(-и) — это в любом случае нужно делать всегда: стараться представить все ситуации, в которых окажется любой ваш код
        board = range(1, 10)
        print('-------------')
        for i in range(3):
            print('|', d_field[board[0+i*3]],
                  '|', d_field[board[1+i*3]],
                  '|', d_field[board[2+i*3]], '|')
            print('-------------')

# СДЕЛАТЬ: очень важно для каждого проекта осмыслить управление переменными в разных областях видимости с учётом передачи по ссылке и по значению:
#  1. какие переменные будут глобальными, какие локальными
#  2. в каких случаях необходимо передавать переменные (или их копии), а в каких работать с глобальными из локальной области видимости
#  3. на каких этапах вы будете создавать копии тех глобальных переменных, которые необходимо передавать по ссылке

# ОТВЕТИТЬ: опишите сценарий, в котором потребуется одним вызовом функции вывести игровые поля из всех СОХРАНЁННЫХ партий
show_field(SAVES)
# ИСПРАВИТЬ: если вы используете сохранённые партии для тестов, то вам нужно написать соответствующий код вне функции — в которую вы передаёте одну партию — именно в таком режиме и должна работать эта функция, что и написано у вас в документации к этой функции


def check_win(turns) -> None:
    """Возвращает логическое значение, есть ли на поле победная комбинация."""
    # ИСПРАВИТЬ: и зачем здесь перебирать все СОХРАНЁННЫЕ партии?
    for players, field in turns.items():
        # ИСПРАВИТЬ: 1. для того, чтобы отсортировать frozenset, не нужно его преобразовывать в кортеж
        #            2. зачем здесь вообще сортировка по алфавиту? может, лучше вывести по порядку: игрок-крестик, игрок-нолик?
        print(f'Игра: {sorted(tuple(players))}')
        players_turns = dict((k, frozenset(v.replace(',','')))
                             for k, v in field.items() if k != 'x')
        print(players_turns)
        for player, made_turns in players_turns.items():
            win_fields = ({'1','2','3'}, {'4','5','6'}, {'7','8','9'}, {'1','4','7'},
                          {'2','5','8'}, {'3','6','9'}, {'1','5','9'}, {'3','5','7'})
            win = False
            for comb in win_fields:
                if comb - made_turns == set():
                    # ИСПРАВИТЬ: это был тестовый вывод - теперь можно его убирать: всё равно о победе заявлять рано
                    print(f'{True} Победил {player} !!!\n')
                    win = True
                    break
            if win:
                break
        else:
            # ИСПРАВИТЬ: это был тестовый вывод - теперь можно его убирать: всё равно о победе заявлять рано
            print(f'{False} Нет победной комбинации ...\n')

# ОТВЕТИТЬ: опишите сценарий, в котором потребуется одним вызовом функции проверить на победные комбинации все СОХРАНЁННЫЕ партии
check_win(SAVES)
# ИСПРАВИТЬ: если вы используете сохранённые партии для тестов, то вам нужно написать соответствующий код вне функции — в которую вы передаёте одну партию — именно в таком режиме и должна работать эта функция, что и написано у вас в документации к этой функции
