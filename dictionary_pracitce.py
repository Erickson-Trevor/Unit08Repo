def diction():
    purse = dict()
    lst = list()
    lst.append(21)
    lst.append(183)
    purse['money'] = 12
    purse['candy'] = 3
    purse['tissues'] = 32
    print(purse)

diction()

def count():
    counts = dict()
    names = ['csev','cwen','zqian','cwen']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1
    print(counts)

    x = counts.get(name,0)