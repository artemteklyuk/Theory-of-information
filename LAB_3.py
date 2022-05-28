import cv2
import random
import numpy as np
import json
from PIL import Image, ImageDraw
from itertools import product
from matplotlib import pyplot as plt
img = cv2.imread('D:\stich1.png', cv2.IMREAD_COLOR)
cv2.imshow('stich', img)
cv2.waitKey(0)
res = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        (b, g, r) = img[i, j]
        print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
print("Высота:"+str(img.shape[0]))
print("Ширина:" + str(img.shape[1]))
print("Количество каналов:" + str(img.shape[2]))
img1 = np.array(img)
with open('file_1.txt','wb') as f:
    for line in img1:
        np.savetxt(f, line, fmt='%d')


file = open("file_1.txt", "r")
for line in file:
   res.append([int(z) for z in line.split()])
#print(res)
for i in range(len(res)):
    for j in range(3):
         res[i][j] = bin(res[i][j])[2:] # срез лишних символов
#print(res)

for i in range(len(res)):
	for j in range(3):
		if (len(res[i][j])<8):
			while(len(res[i][j])<8):
				res[i][j] = '0' + res[i][j] # чтобы было 8 значений и пиксель не изменился
print(res)
MyFile = open('file_2.txt','w')
for item in res:
	MyFile.write('%s\n' % item)

image = Image.open('D:\stich1.png')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

factor = int(input('factor: '))
for i in range(width):
	for j in range(height):
		rand = random.randint(-factor, factor)
		a = pix[i, j][0] + rand
		b = pix[i, j][1] + rand
		c = pix[i, j][2] + rand
		if (a < 0):
			a = 0
		if (b < 0):
			b = 0
		if (c < 0):
			c = 0
		if (a > 255):
			a = 255
		if (b > 255):
			b = 255
		if (c > 255):
			c = 255
		draw.point((i, j), (a, b, c)) # вношу в каждый пиксель ошибку

image.save('D:\simple.png', "PNG")
img = cv2.imread('D:\simple.png', cv2.IMREAD_COLOR)
cv2.imshow('stich2', img)
cv2.waitKey(0)
del draw

I = []
for i in range(len(res)):
	I.append(res[i])


Gsys = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]

HsysT =   [[1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

Gsys = np.array(Gsys)

#поставить весь список пикселей

print("i: ")
print(I)
print("i ")

II = []
for i in range(len(I)):
    II.append(I[i]) #

N = len(Gsys[0])
K = len(Gsys)

for i in range(len(I)):
    for j in range(len(I[i])):
        I[i][j] = list(I[i][j])
for i in range(len(I)):
    for j in range(len(I[i])):
        for k in range(len(I[i][j])):
            I[i][j][k] = int(I[i][j][k])
I = np.array(I) # риведение к удобному виду массива

C = []
for i in range(len(I)):
    for j in range(len(I[i])):
        v = np.reshape(I[i][j], (K,1))
        X = Gsys * v # умножение матриц кодовое слово * на вектора
        c = [0] * N
        for j in range(len(X[0])):
            S = 0
            for l in range(len(X[:, j])): # риведение к удобному виду массива
                if X[:, j][l] == 1 and S == 0:
                    S += int(X[:, j][l])
                elif X[:, j][l] == 1 and S == 1:
                    S -= int(X[:, j][l])
                else:
                    S += int(X[:, j][l])
            c[j] = S
        C.append(c)

while C:
    for i in range(len(II)):
        for j in range(len(II[i])):
            C[0] = "".join(map(str, C[0]))
            II[i][j] = C[0]
            del C[0]
print("c: ")
print(II) # закодированные инф слова без ошибок
print("с ")


for i in range(len(II)):
    for j in range(len(II[i])):
        k1 = random.randint(0, 20) # первая ошибка
        k2 = random.randint(0, 20) # вторая ошибка вносим
        if II[i][j][k1] == "0":
            II[i][j] = II[i][j][:k1] + "1" + II[i][j][k1 + 1:]
        else:
            II[i][j] = II[i][j][:k1] + "0" + II[i][j][k1 + 1:]
        if II[i][j][k2] == "0":
            II[i][j] = II[i][j][:k2] + "1" + II[i][j][k2 + 1:]
        else:
            II[i][j] = II[i][j][:k2] + "0" + II[i][j][k2 + 1:]
print("c': ")
print(II)
print("с' ")



# e
Ie = list(product([0, 1], repeat=N))
Ie = np.array(Ie)
E = []
for i in range(len(Ie)):
    if sum(Ie[i]) <= 2 and sum(Ie[i]) != 0:
        E.append(Ie[i])
E = np.array(E)
#print("e:\n", E)

# S
s = []
for i in range(len(E)):
    w = np.array(E[i])
    w = np.reshape(w, (N, 1))
    Y = HsysT * w
    n = [0] * len(HsysT[0])
    for j in range(len(Y[0])):
        S = 0
        for l in range(len(Y[:,j])):
            if Y[:,j][l] == 1 and S == 0:
                S += int(Y[:,j][l])
            elif Y[:,j][l] == 1 and S == 1:
                S -= int(Y[:,j][l])
            else:
                S += int(Y[:,j][l])
        n[j] = S
    s.append(n)
s = np.array(s)
#print("S:\n", s)

#i, c
I1 = list(product([0, 1], repeat=K))
I1 = np.array(I1)
#print("i:\n", I1)

C1 = []
for i in range(len(I1)):
    v = np.array(I1[i])
    v = np.reshape(v, (K, 1))
    X = Gsys * v
    c = [0] * N
    for j in range(len(X[0])):
        S = 0
        for l in range(len(X[:,j])):
            if X[:,j][l] == 1 and S == 0:
                S += int(X[:,j][l])
            elif X[:,j][l] == 1 and S == 1:
                S -= int(X[:,j][l])
            else:
                S += int(X[:,j][l])
        c[j] = S
    C1.append(c)

C1 = np.array(C1)
#print(C1)
# декодирование, умножаю каждый вектор с ошибкой на HsysT
for i in range(len(II)):
    for j in range(len(II[i])):
        V = []
        v = list(II[i][j])
        for k in range(len(v)):
            v[k] = int(v[k])
        V.append(v)
        V = np.array(V)
        v1 = V[0]
        #print("V: ", V)

        V = np.reshape(V, (len(V[0]),1))
        ss = V * HsysT
        s1 = [0] * len(HsysT[0])
        for k in range(len(ss[0])):
            S = 0
            for l in range(len(ss[:, k])):
                if ss[:, k][l] == 1 and S == 0:
                    S += int(ss[:, k][l])
                elif ss[:, k][l] == 1 and S == 1:
                    S -= int(ss[:, k][l])
                else:
                    S += int(ss[:, k][l])
            s1[k] = S
        s1 = np.array(s1)
        #print("S' =", s1)

        pr1 = False
        for k in range(len(s)):
            k_v = len(s1)
            for l in range(len(s[0])):
                if s1[l] == s[k][l]:
                    k_v -= 1
                if k_v == 0:
                    pr1 = True
                    e1 = E[k]
        if not pr1:
            e1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # каркас из 20 символов
            e1 = np.array(e1)
            #print("e' =", e1)

        S = 0
        c1 = [0] * len(v1)
        for l in range(len(c1)):
            if v1[l] == 1 and e1[l] == 1:
                c1[l] = 0
            elif (v1[l] == 1 and e1[l] == 0) or (v1[l] == 0 and e1[l] == 1):
                c1[l] = 1
            else:
                c1[l] = 0
        #print("c' =", c1)

        for k in range(len(C1)):
            k_b = len(c1)
            for l in range(len(C1[0])):
                if C1[k][l] == c1[l]:
                    k_b -= 1
                if k_b == 0:
                    tl = I1[k].tolist()
                    for m in range(len(tl)):
                        tl[m] = str(tl[m])
                    tl = "".join(tl)
                    II[i][j] = tl
                    #print("i =", tl)



for i in range(len(II)):
	for j in range(3):
		II[i][j]=int(II[i][j],2)
print(II)

img11 = np.array(img1, dtype=np.uint8)[...,::-1]
plt.imshow(img11, interpolation='none')
plt.show()
