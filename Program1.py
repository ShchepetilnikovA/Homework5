with open('text', 'r') as data:
    text = list(data.read().split(' '))
print(text)
text = list(filter(lambda x: 'абв' not in x, text))
with open('text', 'w') as data:
    data.write(" ".join(text))
