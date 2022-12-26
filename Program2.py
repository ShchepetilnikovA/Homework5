from random import randint

flag = (randint(0, 2))
candys = 2021
print(f'it\'s {candys} candys')


def check_input(item):
    while item < 1 or item > 28:
        print('you can move from 1 to 28 candys')
        item = int(input('input amount of candys: '))
    return item


while candys != 0:
    if flag:
        input_candys = check_input(int(input('player one turn: ')))
        candys -= input_candys
        flag = 0
        print(f'it\'s {candys} candys')
        if not candys:
            print('player one win!')
    else:
        print(f'computer take {candys - (candys // 29 * 29)} candys')
        candys -= (candys - (candys // 29 * 29))
        flag = 1
        print(f'it\'s {candys} candys')
        if not candys:
            print('computer win!')
