def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def summator(x, y):
    for i in range(len(SR)):
        rs = []
        for j in range(len(SR[i])):
            rs.append(y[SR[i][j]])
        l = 0
        for k in range(len(rs)):
            if rs[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        x.append(l)

SR = []
s = input("Введите строку: ")

res = ""
for i in range(len(s)):
    if s[i] == "0" or s[i] == "1":
        res += s[i]
    else:
        res = text_to_bits(s)
        #res = ''.join(format(ord(i), 'b') for i in s)
        b = [c for c in res]
        for i in range(len(b)):
            b[i] = int(b[i])

#print(s)
print("Закод строка: " + str(res))
w=[]
for i in range(len(res)):
    w.append(res[i])
    w[i]=int(w[i])

m = [0, 0, 0]
p = []

n = int(input("кол во сумматоров: "))
n1 = n
d = []

for i in range(n):
    print("Ррегистры для", i, "сумматора: ")
    a = input()
    a = a.split()
    for j in range(len(a)):
        a[j] = int(a[j]) - 1
    d.append(a)

for i in range(len(w)):
    m.insert(0, w[i])
    del m[-1]
    sum = 0
    for j in range(len(d)):
        for k in range(len(d[j])):
            sum += m[d[j][k]]
        sum = sum % 2
        p.append(sum)
        sum = 0
while set(m) != {0}: #set - операции над мн вом
    m.insert(0, 0)
    del m[-1]
    sum = 0
    for j in range(len(d)):
        for k in range(len(d[j])):
            sum += m[d[j][k]]
        sum = sum % 2
        p.append(sum)
        sum = 0

P = ""
for i in range(len(p)):
    P += str(p[i])
print("кодирование: ", P)

INFSL = []
while len(P) != 0:
    ck = ""
    for i in range(n):
        ck += P[0]
        P = P.replace(P[0], "", 1)

    reg1 = []
    for i in range(len(m)):
        reg1.append(m[i])
    reg1.insert(0, 0)
    del reg1[-1]
    rez1 = []
    summator(rez1, reg1)

    REZ1 = ""
    for i in range(len(rez1)):
        REZ1 += str(rez1[i])

    reg2 = []
    for i in range(len(m)):
        reg2.append(m[i])
    reg2.insert(0, 1)
    del reg2[-1]
    rez2 = []
    summator(rez2, reg2)

    REZ2 = ""
    for i in range(len(rez2)):
        REZ2 += str(rez2[i])

    if REZ1 == ck and REZ2 != ck:
        INFSL.append(0)
        m = []
        for i in range(len(reg1)):
            m.append(reg1[i])
    elif REZ1 != ck and REZ2 == ck:
        INFSL.append(1)
        m = []
        for i in range(len(reg2)):
            m.append(reg2[i])
    elif len(p) == 0:
        INFSL.append(0)
    elif REZ1 == ck and REZ2 == ck:
        reg4 = []
        for i in range(len(reg2)):
            reg4.append(reg2[i])
        m.insert(0, 0)
        del m[-1]



        reg1 = []
        for i in range(len(m)):
            reg1.append(m[i])
        reg1.insert(0, 0)
        del reg1[-1]
        rez1 = []
        summator(rez1, reg1)

        REZ1 = ""
        for i in range(len(rez1)):
            REZ1 += str(rez1[i])

        reg2 = []
        for i in range(len(m)):
            reg2.append(m[i])
        reg2.insert(0, 1)
        del reg2[-1]
        rez2 = []
        summator(rez2, reg2)

        REZ2 = ""
        for i in range(len(rez2)):
            REZ2 += str(rez2[i])



IS = ""
for i in range(len(res)):
    IS += str(res[i])
IS = IS[:-n1]
print("декодирование: ", IS)
pr1 = False
print(text_from_bits(res))
'''
ck = ""
        for i in range(sumat):
            ck += p[i]
'''