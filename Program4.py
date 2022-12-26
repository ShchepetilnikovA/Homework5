str = 'aaaasssddwwwwweerrrrtttttttttt'
count = 1
for i in range(len(str) - 1):
    if str[i] == str[i + 1]:
        count += 1
    elif count > 9:
        print(f'{9}{str[i]}{count - 9}{str[i]}', end='')
        count = 1
    else:
        print(f'{count}{str[i]}', end='')
        count = 1
    if i == len(str) - 2:
        if count > 9:
            print(f'{9}{str[i + 1]}{count - 9}{str[i + 1]}', end='')
        else:
            print(f'{count}{str[i + 1]}', end='')

