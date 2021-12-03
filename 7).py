s=input('Podaj słowo: ')
def count_chars(słowo):
    dict = {}
    for n in słowo:
        x = dict.keys()
        if n in x:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(count_chars(s))