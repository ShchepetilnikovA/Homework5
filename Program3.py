from random import randint

field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def print_field():
    for i in range(len(field)):
        field_str = " | ".join(field[i])
        print(field_str, end='\n---------\n')

def who_win(field, player, block):
    if block > 2:
        if field[0[0]] == field[0[1]] == field[0[2]]:
            print(f'player {player} win!')
        elif field[0[0]] == field[1[0]] == field[2[0]]:
            print(f'player {player} win!')
        elif field[1[0]] == field[1[1]] == field[1[2]]:
            print(f'player {player} win!')
        elif field[2[0]] == field[2[1]] == field[2[2]]:
            print(f'player {player} win!')
        elif field[0[0]] == field[1[1]] == field[2[2]]:
            print(f'player {player} win!')
        elif field[2[0]] == field[1[1]] == field[0[2]]:
            print(f'player {player} win!')
        elif field[1[0]] == field[1[1]] == field[1[2]]:
            print(f'player {player} win!')
        elif field[2[0]] == field[2[1]] == field[2[2]]:
            print(f'player {player} win!')

flag = randint(0, 2)
if flag:
    print_field()
    print(f'it\'s player {flag} turn')
    turn = input('input number on field')
    turn.index
