str = '4a3s2d5w2e4r9t1t'
str = list(str)


def out(count, value):
    count = int(count)
    while count > 0:
        count -= 1
        print(value, end='')


for i in range(0, len(str), 2):
    out(str[i], str[i + 1])
