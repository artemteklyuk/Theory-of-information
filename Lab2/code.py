import re

def function1(txt, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(txt.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8)) # преобразование в двоичную строку
# to bits
def function2(file):
    txt_bits = function1(file)
    i = []
    for k, l in enumerate(txt_bits):
        if int(l) == 1:
            i.append(k)
    return i
# to list of indexes
def function3(expression):
    symbols = "!@#$%^&*()_+=/><.,'№;:?"
    regexp = r"([a-zA-Z])"
    match = re.search(regexp, expression)
    if (match is None) and (symbols not in expression):
        return True
    else:
        return False
#sybmols
def function4(expression):
    symbols = "!@#$%^&*()+=/><.,'№;:?_"
    regexp = r"([a-zA-Z])"
    regexp1 = "4567890"
    match = re.search(regexp, expression)
    match1 = re.search(regexp1, expression)
    if (match is None) and (match1 is None) and (symbols not in expression):
        return True
    else:
        return False

def polinom(g, file):
    global max #объявляем глобальную переменную
    i = function2(file)
    for k, m in enumerate(g):
        for l, n in enumerate(g[k]):
            g[k][l] = int(g[k][l]) - 1          # переводим к виду степеней икс в сумматоры
    c = []
    for k, m in enumerate(g):
        a = []
        for l, n in enumerate(g[k]):
            for p, q in enumerate(i):           # суммируем кодированное слово и сумматоры
                d = int(n) + int(q)
                a.append(d)
                a.sort()
        c.append(a)
    count = -1
    code_word = []
    for o in range(len(c)):
        for k in range(len(c[o]) - 1):
            if (c[o][k] == c[o][k + 1]) or (c[o][k] == count):
                count = c[o][k]                         # если есть одинаковые степени мы присваем им значеним -1
                c[o][k] = -1
                c[o][k] = -1
    for o in range(len(c)):
        while c[o].count(-1) != 0:
            c[o].remove(-1)                             # все -1 удаляем
    max = max(map(max, c))                              # обновляю список max
    for k, m in enumerate(c):
        min = 0
        while min != max:
            if min in c[k]:                             # степени икса переводим к полиному
                code_word.append(1)
            else:
                code_word.append(0)
            min += 1
    return code_word

# получаем полином и все решения