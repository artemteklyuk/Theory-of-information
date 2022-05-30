from tkinter import *
from tkinter import messagebox
from sympy import *
from mpmath import *
from math import *
import re
import numpy as np
import random

# Переделываем двоичную последовательность во многочлен
def perevod(posled): # вход: int последовательность 1 и 0
    rez_str = []
    for i in range(len(posled)):# перебираем символы в двоичном ногочлене
        if posled[i] == 1 and len(posled) - 1 - i != 1 and len(posled) - 1 - i != 0: # если символ = 1 и он не последний и не предпоследний
            rez_str.append("x**") # то ставлю на его место х**
            rez_str.append(str(len(posled) - 1 - i)) # степень в зависимости от его позиции
            rez_str.append("+") # и +
        if len(posled) - 1 - i == 1 and posled[i] == 1: # если символ предпоследний и = 1
            rez_str.append("x") # то ставлю на его место х
            rez_str.append("+") # и +
        if len(posled) - 1 - i == 0 and posled[i] == 1:  # если символ последний и = 1
            rez_str.append("1") # то ставлю на его место 1
        if posled[i] == 0: # если символ = 0, то он нас не интересует
            pass
    if rez_str[len(rez_str) - 1] == "+":  # удоляю + в конце если он есть
        rez_str.pop(len(rez_str) - 1)
    print(rez_str)
    new_rez = [] # создаю пустой массив для преоразования многочлена в удобный вид
    for i in range(len(rez_str)): # перебираю элементы многочлена
        if rez_str[i] == "x**": # если элемент = х**
            new_rez[i: i + 2] = [''.join(rez_str[i: i + 2])] # то соединяю его со следующим чтобы получилось например х**3
            new_rez.append("+") # и добавляю +
        if rez_str[i] == "x": # если элемент = х
            new_rez.append("x") # то просто добавляю его в новый массив
            new_rez.append("+") # и добавляю +
        if rez_str[i] == "1": #если элемент = 1
            new_rez.append("1") # то просто добавляю его в новый массив
    if new_rez[len(new_rez) - 1] == "+": # удоляю + в конце если он есть
        new_rez.pop(len(new_rez) - 1)
    return new_rez # выход: str многочлен
#вношу 1 ошибку
def mistake(inf_slovo): # вход inf_slovo без ошибки
    k1 = random.randint(1, len(inf_slovo)-1) # первая ошибка
    print(k1)
    if inf_slovo[k1] == 0:
        inf_slovo = inf_slovo[:k1] + [1] + inf_slovo[k1 + 1:]
    else:
        inf_slovo = inf_slovo[:k1] + [0] + inf_slovo[k1 + 1:]
    return [inf_slovo, k1]
# выход inf_slovo с ошибкой

#конвертируем полином и символьные слова в двоичный вид
#вход: строка
def conventor(stroka):
    stroka = stroka.split(" ")
    stroka_List = list(stroka)
    print(stroka, "входная строка")
    stepen_List = []
    for i in range(len(stroka_List)):  # создание списка степеней входящих в делимое
        if len(stroka_List[i]) == 4:
            stepen_List.append(stroka_List[i][3])
        elif len(stroka_List[i]) == 5:
            stepen_List.append(stroka_List[i][3:5])
        elif stroka_List[i] == "x":
            stepen_List.append("1")
        elif stroka_List[i] == "1":
            stepen_List.append("0")
    stepen_List.sort()
    for i in range(len(stepen_List)):
        stepen_List[i] = int(stepen_List[i])
    print("лист степеней делимого полинома:", stepen_List)
    max_stepen = int(max(stepen_List))
    for i in range(len(stepen_List)):
        stepen_List[i] = str(stepen_List[i])
    print("максимальная степень делимого полинома:", max_stepen)
    stroka_List_0_1 = [0]*(max_stepen + 1)    #создание делимого в двоичном коде
    for i in range(len(stepen_List)):
        stroka_List_0_1[int(stepen_List[i])] = 1

    stroka_List_0_1.reverse()
    print("делимое в двоичном коде: ", stroka_List_0_1)
    print("Dелимое:", stroka_List)
    return [stroka_List_0_1, max_stepen]
#выход: словарь строки в двоичом коде

# КАЛЬКУЛЯТОР ДЛЯ 3 И 4 СПОСОБОВ
#вход: строка делимого и делителя
def coding(delimoe, delitel):
    delimoe = delimoe.split(" ")
    delimoe_List = list(delimoe)

    stepen_List = []

    for i in range(len(delimoe_List)):  # создание списка степеней входящих в делимое
        if len(delimoe_List[i]) == 4:
            stepen_List.append(delimoe_List[i][3])
        elif len(delimoe_List[i]) == 5:
            stepen_List.append(delimoe_List[i][3:5])
        elif delimoe_List[i] == "x":
            stepen_List.append("1")
        elif delimoe_List[i] == "1":
            stepen_List.append("0")
    stepen_List.sort()
    for i in range(len(stepen_List)):
        stepen_List[i] = int(stepen_List[i])
    print("лист степеней делимого полинома:", stepen_List)
    max_stepen = int(max(stepen_List))
    for i in range(len(stepen_List)):
        stepen_List[i] = str(stepen_List[i])
    print("максимальная степень делимого полинома:", max_stepen)
    delimoe_List_0_1 = [0] * (max_stepen + 1)  # создание делимого в двоичном коде
    for i in range(len(stepen_List)):
        delimoe_List_0_1[int(stepen_List[i])] = 1

    delimoe_List_0_1.reverse()
    print("делимое в двоичном коде: ", delimoe_List_0_1)
    print("Dелимое:", delimoe_List)

    delitel = delitel.split(" ")
    delitel_List = list(delitel)

    stepen_List_2 = []
    for i in range(len(delitel_List)):  # создание списка степеней входящих в делитель
        if len(delitel_List[i]) == 4:
            stepen_List_2.append(delitel_List[i][3])
        elif len(delitel_List[i]) == 5:
            stepen_List_2.append(delitel_List[i][3:5])
        elif delitel_List[i] == "x":
            stepen_List_2.append("1")
        elif delitel_List[i] == "1":
            stepen_List_2.append("0")
    stepen_List_2.sort()
    print("лист степеней делителя полинома:", stepen_List_2)
    for i in range(len(stepen_List_2)):
        stepen_List_2[i] = int(stepen_List_2[i])
    max_stepen_2 = int(max(stepen_List_2))
    for i in range(len(stepen_List_2)):
        stepen_List_2[i] = str(stepen_List_2[i])
    print("максимальная степень делителя полинома:", max_stepen_2)
    delitel_List_0_1 = [0] * (max_stepen_2 + 1)  # создание делителя в двоичном коде
    for i in range(len(stepen_List_2)):
        delitel_List_0_1[int(stepen_List_2[i])] = 1

    delitel_List_0_1.reverse()
    print("делитель в двоичном коде: ", delitel_List_0_1)
    print("Dелитель:", delitel_List)

    zapas_delimoe = delimoe_List_0_1.copy()
    p = 0
    rez = ["1"]
    Chet_nuley_del_vsego = 0
    while len(delitel_List_0_1) <= len(delimoe_List_0_1):  # само деление двоичного делимого на делитель
        print(len(delimoe_List_0_1))
        new_delimoe_0_1 = []  # новое делимое которое постоянно образуется в ходе деления столбиком
        for i in range(len(delitel_List_0_1)):
            index_and = delitel_List_0_1[i] ^ delimoe_List_0_1[i]  # побитовое умножение предыдущего делимого на новое
            new_delimoe_0_1.append(index_and)  # образование следующей строки делимого
            print(new_delimoe_0_1)
        delimoe_List_0_1.clear()
        delimoe_List_0_1 = new_delimoe_0_1.copy()  # присваивание нового значения делимого старому
        print(len(delimoe_List_0_1))
        j = 0
        Chet_nuley_del = 0
        while j < len(delimoe_List_0_1):  # считаем и убираем ненужные нули в начале выражения
            if delimoe_List_0_1[j] == 0:
                delimoe_List_0_1.pop(j)
                j = j
                Chet_nuley_del += 1
            else:
                break
        print("сколько убрано нулей", Chet_nuley_del)
        print("do", delimoe_List_0_1)
        Chet_nuley_del_vsego += Chet_nuley_del
        Chet_nuley_add = 0

        if len(zapas_delimoe) != len(delitel_List_0_1):  # сношу в конец выражения новый бит, если это требуется
            q = 0
            while len(delimoe_List_0_1) < len(delitel_List_0_1):
                dobavochny_index_delimogo = p + len(delitel_List_0_1)  # узнаю какой индекс с делимого снести, считаю количество уже снесенных индексов и прибавляю к длинне делителя
                if dobavochny_index_delimogo == len(zapas_delimoe):
                    break
                delimoe_List_0_1.append(zapas_delimoe[dobavochny_index_delimogo])  # сношу найденный индекс
                Chet_nuley_add += 1
                p += 1
        if Chet_nuley_add == 1 and len(delimoe_List_0_1) < len(delitel_List_0_1):
            rez.append("0")
        if Chet_nuley_add == 1 and len(delimoe_List_0_1) == len(delitel_List_0_1):
            rez.append("1")
        elif Chet_nuley_add > 1:
            for i in range(Chet_nuley_add-1):
                rez.append("0")
            if len(delimoe_List_0_1) == len(delitel_List_0_1):
                rez.append("1")
            else:
                rez.append("0")





        print("сколько добавлено индексов", Chet_nuley_add)  # считаю скольк обыло добавленно индексов



    else:
        print(
            Chet_nuley_del_vsego)  # добавляю нули обратно в начало конечного остатка, чтобы сравнить его длину с делимым и убедиться что сносить нечего
        y = 0
        while Chet_nuley_del_vsego > y:
            delimoe_List_0_1.insert(0, 0)
            y += 1
        print(delimoe_List_0_1)
        o = 0
        if len(delimoe_List_0_1) != len(
                zapas_delimoe):  # если длины не сходятся то сношу оставшиеся биты по последующему индексу

            dobavochny_index_delimogo += 1
            print(zapas_delimoe)
            delimoe_List_0_1.append(zapas_delimoe[dobavochny_index_delimogo])
            o += 1
        j = 0
        while j < len(delimoe_List_0_1):  # убираем ненужные нули в начале выражения
            if delimoe_List_0_1[j] == 0:
                delimoe_List_0_1.pop(j)
                j = j
            else:
                break
        if o > 0:
            print("Конечный остаток от деления:", delimoe_List_0_1)
        else:
            print("Конечный остаток от деления:", delimoe_List_0_1)

    for i in range(len(rez)):
        rez[i] = int(rez[i])
    print(rez, "результат деления")

    rezultat = []
    indx = 0
    rez.reverse()
    for i in range(len(rez)):
        if rez[i] == 1:
            if indx == 0:
                rezultat.insert(0, 1)
                indx += 1
            elif indx == 1:
                rezultat.insert(0, "x")
                indx += 1
            elif indx > 1:
                rezultat.insert(0, "x" + "**" + str(indx))
                indx += 1
        else:
            indx += 1
    print(rezultat)
    str_rezultat = " + ".join(map(str, rezultat))
    print("Результат деления: ", str_rezultat)

    ostatok = []
    ind = 0
    delimoe_List_0_1.reverse()
    for i in range(len(delimoe_List_0_1)):
        if delimoe_List_0_1[i] == 1:
            if ind == 0:
                ostatok.insert(0, 1)
                ind += 1
            elif ind == 1:
                ostatok.insert(0, "x")
                ind += 1
            elif ind > 1:
                ostatok.insert(0, "x" + "**" + str(ind))
                ind += 1
        else:
            ind += 1
    print(ostatok)
    str_ostatok = " + ".join(map(str, ostatok))
    print("Остаток: ", str_ostatok)
    return [str_ostatok, str_rezultat]
#выход: строка остатка, строка результата деления

def entry_to_int_list(ent_str):
    ent_str = ent_str.split(" ")
    List = list(ent_str)
    for i in range(len(List)):
        List[i] = int(List[i])
    return List

#ПРИЛОЖЕНИЕ
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Мое приложение")
tk.configure(bg="white")
tk.resizable(0, 0)
tk.geometry("1200x1200")
tk.wm_attributes("-topmost", 1)

frame1 = Frame(width=250, height=340, bg = "white")
frame1.grid(column = 0, row = 0, sticky="w")
frame2 = Frame(width=250, height=340, bg = "white")
frame2.grid(column = 0, row = 1, sticky="n")
frame3 = Frame(width=400, height=340, bg ="white")
frame3.grid(column=1, row=0, sticky="n")
frame3.grid_propagate(False)
frame4 = Frame(width=400, height=250, bg ="blue")
frame4.grid(column=1, row=1, sticky="n")
frame4.grid_propagate(False)
frame5 = Frame(width=400, height=340, bg ="green")
frame5.grid(column=2, row=0, sticky="n")
frame5.grid_propagate(False)
# Вводим данные
dano_label = Label(frame1, text="Дано", font=("Roboto", 30), bg= "white").place(x=50,y=0)

vvod_label = Label(text="Введите полином", font=("Roboto", 10), bg = "white").place(x=9, y=300, width=234, height=40)

def calculate(operation):
    global formula

    if operation == "C":
        formula = ""
    elif operation == "del":
        formula = formula[0:-1]
    else:
        if formula == "0":
            formula = ""
        formula += operation

    label_text.configure(text=formula)
    print(formula)



formula = "0"
label_text = Label(frame1, text=formula, font=("Roboto", 10), bg = "green")
label_text.place(x=9, y=250, width=234, height=40)


label_vvedennyi_polinom = Label(frame2, bg ="yellow")
label_vvedennyi_polinom.grid(column = 0, row = 0, sticky="w")

entr_dvoich=Entry(frame2)
entr_dvoich.grid(column = 0, row=1, sticky="w")


label_m = Label(frame2, text="m =")
label_m.grid(column=0, row=16, sticky="w")
entry_m = Entry(frame2)
entry_m.grid(column=0, row=16, sticky="e")
# подтверждаю введенный при помощи интерфейса полином и создаю следующую кнопку для ввода информационных слов

def OK_polinom():
    global m0
    global vvedennyi_polinom_mew
    global vvedennyi_polinom
    vvedennyi_polinom = formula.split('+')
    j = 1
    for i in range(len(vvedennyi_polinom)):
        vvedennyi_polinom.insert(i+j, "+")
        j+=1
    vvedennyi_polinom.pop(len(vvedennyi_polinom)-1)

    q =1
    for i in range(len(vvedennyi_polinom)):
        vvedennyi_polinom.insert(i+q, " ")
        q+=1
    vvedennyi_polinom.pop(len(vvedennyi_polinom)-1)
    print(vvedennyi_polinom," введенный полином ")
    vvedennyi_polinom_mew = "".join(map(str,vvedennyi_polinom))


    label_vvedennyi_polinom.configure(text="Полином: " + vvedennyi_polinom_mew)
    entr_dvoich.delete(0,END)
    entr_dvoich.insert(0, conventor(vvedennyi_polinom_mew)[0]) # вывод полинома в двоичной системе
    m0=conventor(vvedennyi_polinom_mew)[1]
    entry_m.delete(0,END)
    entry_m.insert(0,m0) # вывод максимальной степени m

    print(vvedennyi_polinom_mew," введенный полином мю")


new_Button = Button(frame1, text="OK", command= OK_polinom, bg ="silver", font=("Roboto", 10))
new_Button.place(x=127, y=204, width=116, height=40)




label_vvedennyi_inf_slovo_1 = Label(frame2, bg ="yellow")
label_vvedennyi_inf_slovo_1.grid(column = 0, row = 3, sticky="w")
label_vvedi = Label(frame2, text="Введите информационное слово 1: ", bg="white")
label_vvedi.grid(column = 0, row = 2, sticky="w")

entr_dvoich_2=Entry(frame2)
entr_dvoich_2.grid(column = 0, row=4, sticky="w")

label_k = Label(frame2, text="k(Длина инф. слова) =")
label_k.grid(column=0, row=14, sticky="w")
entry_k = Entry(frame2)
entry_k.grid(column=0, row=14, sticky="e")
def OK_inf_slovo_1():
    global vvedennyi_inf_slovo_1_mew
    vvedennyi_inf_slovo_1 = formula.split('+')
    j = 1

    for i in range(len(vvedennyi_inf_slovo_1)):
        vvedennyi_inf_slovo_1.insert(i + j, "+")
        j += 1
    vvedennyi_inf_slovo_1.pop(len(vvedennyi_inf_slovo_1) - 1)
    print(vvedennyi_inf_slovo_1)
    q = 1
    for i in range(len(vvedennyi_inf_slovo_1)):
        vvedennyi_inf_slovo_1.insert(i + q, " ")
        q += 1
    vvedennyi_inf_slovo_1.pop(len(vvedennyi_inf_slovo_1) - 1)
    vvedennyi_inf_slovo_1_mew = "".join(map(str, vvedennyi_inf_slovo_1))
    print(vvedennyi_inf_slovo_1_mew)
    entr_dvoich_2.delete(0, END)
    entr_dvoich_2.insert(0,conventor(vvedennyi_inf_slovo_1_mew)[0])  # вывод инф слова в двоичной системе
    global k1
    k1=conventor(vvedennyi_inf_slovo_1_mew)[1] + 1 #1-e инф. слово задает максимальную длину всех инф. слов
    print(conventor(vvedennyi_inf_slovo_1_mew))
    label_vvedennyi_inf_slovo_1.configure(text=vvedennyi_inf_slovo_1_mew)
    entry_k.delete(0, END)
    entry_k.insert(0, k1)
new_Button_2 = Button(frame2, text="OK", command=OK_inf_slovo_1, bg ="silver", font=("Roboto", 10))
new_Button_2.grid(column = 0, row = 5, sticky="e")





label_vvedi_2 = Label(frame2, text="Введите информационное слово 2: ", bg="white")
label_vvedi_2.grid(column = 0, row = 6, sticky="w")
label_vvedennyi_inf_slovo_2 = Label(frame2, bg="yellow")
label_vvedennyi_inf_slovo_2.grid(column = 0, row = 7, sticky="w")

entr_dvoich_3=Entry(frame2)
entr_dvoich_3.grid(column = 0, row=8, sticky="w")
def OK_inf_slovo_2():
    global vvedennyi_inf_slovo_2_mew
    vvedennyi_inf_slovo_2 = formula.split('+')
    j = 1

    for i in range(len(vvedennyi_inf_slovo_2)):
        vvedennyi_inf_slovo_2.insert(i + j, "+")
        j += 1
    vvedennyi_inf_slovo_2.pop(len(vvedennyi_inf_slovo_2) - 1)
    print(vvedennyi_inf_slovo_2)
    q = 1
    for i in range(len(vvedennyi_inf_slovo_2)):
        vvedennyi_inf_slovo_2.insert(i + q, " ")
        q += 1
    vvedennyi_inf_slovo_2.pop(len(vvedennyi_inf_slovo_2) - 1)
    vvedennyi_inf_slovo_2_mew = "".join(map(str, vvedennyi_inf_slovo_2))
    k2 = conventor(vvedennyi_inf_slovo_2_mew)[1] + 1
    if k1 == k2:
        print(vvedennyi_inf_slovo_2_mew, "k1 == k2")
        label_vvedennyi_inf_slovo_2.configure(text=vvedennyi_inf_slovo_2_mew)
        entr_dvoich_3.delete(0,END)
        entr_dvoich_3.insert(0, conventor(vvedennyi_inf_slovo_2_mew)[0]) # 1-e инф. слово задает максимальную длину всех инф. слов
    elif k1 > k2:
        c = k1 - k2

        stroka = conventor(vvedennyi_inf_slovo_2_mew)[0]
        while c != 0:
            stroka.insert(0,0)
            c -= 1
        label_vvedennyi_inf_slovo_2.configure(text=vvedennyi_inf_slovo_2_mew)
        entr_dvoich_3.delete(0, END)
        entr_dvoich_3.insert(0, stroka)  # вывод инф слова в двоичной системе
        print(vvedennyi_inf_slovo_2_mew, "k1 > k2")
    else:
        entr_dvoich_3.delete(0, END)
        entr_dvoich_3.insert(0, "Еще разок")  #при попытке ввода более длинного слова система попросит еще раз ввести слово

new_Button_3 = Button(frame2, text="OK", command=OK_inf_slovo_2, bg="silver", font=("Roboto", 10))
new_Button_3.grid(column = 0, row = 9, sticky="e")




label_vvedi_3 = Label(frame2, text="Введите информационное слово 3: ", bg="white") # Введите информационное слово 3:
label_vvedi_3.grid(column = 0, row = 10, sticky="w")
label_vvedennyi_inf_slovo_3 = Label(frame2, bg="yellow") # вывод информационное слово 3:
label_vvedennyi_inf_slovo_3.grid(column = 0, row = 11, sticky="w")

entr_dvoich_4=Entry(frame2)
entr_dvoich_4.grid(column = 0, row=12, sticky="w") # сюда выводится двоичное значение 3го слова
label_n = Label(frame2, text="n =")
label_n.grid(column=0, row=15, sticky="w")
entry_n = Entry(frame2)
entry_n.grid(column=0, row=15, sticky="e")
def OK_inf_slovo_3():
    global vvedennyi_inf_slovo_3_mew
    global n
    vvedennyi_inf_slovo_3 = formula.split('+')
    j = 1

    for i in range(len(vvedennyi_inf_slovo_3)):
        vvedennyi_inf_slovo_3.insert(i + j, "+")
        j += 1
    vvedennyi_inf_slovo_3.pop(len(vvedennyi_inf_slovo_3) - 1)
    print(vvedennyi_inf_slovo_3)
    q = 1
    for i in range(len(vvedennyi_inf_slovo_3)):
        vvedennyi_inf_slovo_3.insert(i + q, " ")
        q += 1
    vvedennyi_inf_slovo_3.pop(len(vvedennyi_inf_slovo_3) - 1)
    vvedennyi_inf_slovo_3_mew = "".join(map(str, vvedennyi_inf_slovo_3))
    k3 = conventor(vvedennyi_inf_slovo_3_mew)[1] + 1
    if k1 == k3:
        print(vvedennyi_inf_slovo_3_mew, "k1 == k3")
        label_vvedennyi_inf_slovo_3.configure(text=vvedennyi_inf_slovo_3_mew) # 1-e инф. слово задает максимальную длину всех инф. слов
        entr_dvoich_4.delete(0,END)
        entr_dvoich_4.insert(0, conventor(vvedennyi_inf_slovo_3_mew)[0]) # вывод инф слова в двоичной системе
    elif k1 > k3:
        c = k1 - k3

        stroka = conventor(vvedennyi_inf_slovo_3_mew)[0]
        while c != 0:
            stroka.insert(0,0)
            c -= 1
        label_vvedennyi_inf_slovo_3.configure(text=vvedennyi_inf_slovo_3_mew)
        entr_dvoich_4.delete(0, END)
        entr_dvoich_4.insert(0, stroka)  # вывод инф слова в двоичной системе
        print(stroka, "k1 > k2")
    else:
        entr_dvoich_4.delete(0, END)
        entr_dvoich_4.insert(0, "Еще разок")  #при попытке ввода более длинного слова система попросит еще раз ввести слово
    n = m0 + k1
    entry_n.delete(0,END)
    entry_n.insert(0,n)


new_Button_4 = Button(frame2, text="OK", command=OK_inf_slovo_3, bg="silver", font=("Roboto", 10))
new_Button_4.grid(column = 0, row = 13, sticky="e")


# Создаем кнопки
buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "del", "C", "x", "**", "+"]
x = 9
y = 70
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    Button(frame1, text=button, bg="silver", font=("Roboto", 10), command=get_lbl).place(x=x, y=y, width=57, height=39)
    x+= 59
    if x > 200:
        x = 9
        y+=45


new_Button_1 = Button(frame1, text="OK", command= OK_polinom, bg ="silver", font=("Roboto", 10)) #кнопка вывода полинома и полинома в двоичном виде
new_Button_1.place(x=127, y=204, width=116, height=40)



# 1 способ кодирования

lbl_1_sp = Label(frame3, text="1 Способ", font=("Roboto", 20), bg= "white") #1 Способ
lbl_1_sp.grid(column = 1, row = 0, sticky = "wn")

lbl_1_1 = Label(frame3, text="c = i * G", font="bold", bg= "white") #c = i * G
lbl_1_1.grid(column = 1, row = 2, sticky = "wn")

lbl_1_2 = Label(frame3, text="G = ", font="bold", bg= "white") # G =
lbl_1_2.grid(column = 1, row = 3, sticky = "w")

lbl_c_1 = Label(frame3, text="C1 = ", bg= "white") # C1 =
lbl_c_1.grid(column = 1, row = 6, sticky = "w")
entr_c_1 = Entry(frame3)
entr_c_1.grid(column = 1, row = 6, sticky = "e")

lbl_c_1 = Label(frame3, text="C2 = ", bg= "white") # C2 =
lbl_c_1.grid(column = 1, row = 7, sticky = "w")
entr_c_2 = Entry(frame3)
entr_c_2.grid(column = 1, row = 7, sticky = "e")

lbl_c_3 = Label(frame3, text="C3 = ", bg= "white") #C3 =
lbl_c_3.grid(column = 1, row = 8, sticky = "w")
entr_c_3 = Entry(frame3)
entr_c_3.grid(column = 1, row = 8, sticky = "e")

entr_check = Entry(frame3, width=1 )
entr_check.grid(column = 1, row = 1, sticky = "w")
def Matrix():
    n = int(entry_n.get())
    k = int(entry_k.get())
    txt_1_2 = Text(frame3, width=n*3, height=k)
    txt_1_2.grid(column=1, row=3, sticky="e")
    txt_1_3 = Text(frame3, width=9, height=k, bg = "yellow")
    txt_1_3.grid(column=2, row=3, sticky="e", padx = 15)
    polinom = conventor(vvedennyi_polinom_mew)[0]

    vector_1 = entry_to_int_list(entr_dvoich_2.get()) # получение инф. слов в двоичной системе
    vector_2 = entry_to_int_list(entr_dvoich_3.get()) # получение инф. слов в двоичной системе
    vector_3 = entry_to_int_list(entr_dvoich_4.get()) # получение инф. слов в двоичной системе
    d = n - len(polinom)
    if len(polinom) < n:
        while d !=0:
            polinom.insert(0,0)
            d -= 1
    Matrix = []
    print(Matrix)

    while k != 0: # создание матрицы путем сдвига полинома влево на 1 символ ( сдвигаю столько раз, насколько отличаются длина полинома и число n
        print(polinom)
        entr_check.insert(0, polinom)
        Matrix.append(entr_check.get())
        entr_check.delete(0, END)
        polinom.pop(0) #удаление первого символа
        polinom.append(0) #добавление нуля в конец
        k-=1
    global MATRIX
    global VECTOR_ar
    MATRIX = []
    for i in range(len(Matrix)):
        Matrix[i].split(" ")
        Matrix_list = list(Matrix[i])
        for k in range(int(len(Matrix_list)/2)):
            Matrix_list.pop(k+1)
        MATRIX.append(Matrix_list)
    print(MATRIX)
    for n, i in enumerate(MATRIX):  # перевод строчных символов в Integer
        for k, j in enumerate(i):
            MATRIX[n][k] = int(j)

    MATRIX_ar = np.array(MATRIX)

    print(MATRIX_ar)
    VECTOR_ar_ = np.array([vector_1, vector_2, vector_3]) #создаю матрицу из символьных слов
    VECTOR_ar = []
    for i in range(len(VECTOR_ar_)):  # Отзеркаливаю ее по вертикали
        it = []
        for j in range(len(VECTOR_ar_[i])):
            it.insert(0, VECTOR_ar_[i][j])
        VECTOR_ar.append(it)
    print(VECTOR_ar)
    VECTOR_ar_T = np.transpose(VECTOR_ar) # Транспонирую для наглядного сопоставления с матрицей
    print(VECTOR_ar_T)


    txt_1_2.insert(0.0, MATRIX_ar)
    txt_1_3.insert(0.0, VECTOR_ar_T)


def umnojenie():
    global umnoj
    global umnoj1
    global umnoj2

    mass_ind = []  # Начало алгоритма посимвольного умножения строк матрицы, соответствующих еденицам i-тых инф. слов
    for i in range(len(VECTOR_ar[0])):
        if VECTOR_ar[0][i] == 1:
            mass_ind.append(i)
    umnoj = [0]*len(MATRIX[mass_ind[0]])


    for k in range(len(umnoj)):
        umnoj.append(umnoj[k] ^ MATRIX[mass_ind[0]][k])
    del umnoj[0:len(MATRIX[mass_ind[0]])]
    for t in range(len(mass_ind)-1):
        for j in range(len(MATRIX[mass_ind[t]])):
            umnoj.append(umnoj[j] ^ MATRIX[mass_ind[t+1]][j])
        del umnoj[0:len(MATRIX[mass_ind[0]])]

    entr_c_1.delete(0, END)
    entr_c_1.insert(0,umnoj)

    mass_ind_2 = []  # Начало алгоритма посимвольного умножения строк матрицы, соответствующих еденицам i-тых инф. слов
    for i in range(len(VECTOR_ar[1])):
        if VECTOR_ar[1][i] == 1:
            mass_ind_2.append(i)
    umnoj1 = [0] * len(MATRIX[mass_ind_2[0]])
    for k in range(len(umnoj1)):
        umnoj1.append(umnoj1[k] ^ MATRIX[mass_ind_2[0]][k])
    del umnoj1[0:len(MATRIX[mass_ind_2[0]])]
    for t in range(len(mass_ind_2) - 1):
        for j in range(len(MATRIX[mass_ind_2[t]])):
            umnoj1.append(umnoj1[j] ^ MATRIX[mass_ind_2[t + 1]][j])
        del umnoj1[0:len(MATRIX[mass_ind_2[0]])]

    print(umnoj1)
    entr_c_2.delete(0, END)
    entr_c_2.insert(0, umnoj1)

    mass_ind_3 = []  # Начало алгоритма посимвольного умножения строк матрицы, соответствующих еденицам i-тых инф. слов
    for i in range(len(VECTOR_ar[2])):
        if VECTOR_ar[2][i] == 1:
            mass_ind_3.append(i)
    umnoj2 = [0] * len(MATRIX[mass_ind_3[0]])

    for k in range(len(umnoj2)):
        umnoj2.append(umnoj2[k] ^ MATRIX[mass_ind_3[0]][k])
    del umnoj2[0:len(MATRIX[mass_ind_3[0]])]
    for t in range(len(mass_ind_3) - 1):
        for j in range(len(MATRIX[mass_ind_3[t]])):
            umnoj2.append(umnoj2[j] ^ MATRIX[mass_ind_3[t + 1]][j])
        del umnoj2[0:len(MATRIX[mass_ind_3[0]])]

    entr_c_3.delete(0, END)
    entr_c_3.insert(0, umnoj2)

but_1_sp = Button(frame3, text="вставить матрицу G", command=Matrix) # кнопка "вставить матрицу G"
but_1_sp.grid(column=1, row = 1, sticky="w")

but_1_sp_2 = Button(frame3, text="Закодировать", command=umnojenie) # кнопка "Закодировать"
but_1_sp_2.grid(column=1, row = 5, sticky="w")


lbl_2_sp = Label(frame4, text="2 Способ", font=("Roboto", 20), bg= "white") #2 Способ
lbl_2_sp.grid(column = 1, row = 0, sticky = "wn")

lbl_2_1 = Label(frame4, text="C(x) = i(x)*g(x)",font = (12), bg= "white") #формула
lbl_2_1.grid(column = 1, row = 1, sticky = "wn")

lbl_cx_1 = Label(frame4, text="C1(x) = ", bg= "white") # C1(x) =
lbl_cx_1.grid(column = 1, row = 2, sticky = "w")
entr_cx_1 = Entry(frame4)
entr_cx_1.grid(column = 1, row = 2, sticky = "w", padx = 50)

lbl_cx_2 = Label(frame4, text="C2(x) = ", bg= "white") # C2(x) =
lbl_cx_2.grid(column = 1, row = 3, sticky = "w")
entr_cx_2 = Entry(frame4)
entr_cx_2.grid(column = 1, row = 3, sticky = "w", padx = 50)

lbl_cx_3 = Label(frame4, text="C3(x) = ", bg= "white") #C3(x) =
lbl_cx_3.grid(column = 1, row = 4, sticky = "w")
entr_cx_3 = Entry(frame4)
entr_cx_3.grid(column = 1, row = 4, sticky = "w", padx = 50)

def X_umbojenie(): # Переделываем двоичную последовательность во многочлен

    new = perevod(umnoj) # Переделываем двоичную последовательность во многочлен
    new1 = perevod(umnoj1) # Переделываем двоичную последовательность во многочлен
    new2 = perevod(umnoj2) # Переделываем двоичную последовательность во многочлен

    entr_cx_1.delete(0,END)
    entr_cx_1.insert(0,"(")
    entr_cx_1.insert(END, vvedennyi_polinom_mew)
    entr_cx_1.insert(END, ")")
    entr_cx_1.insert(END, " * ")
    entr_cx_1.insert(END, "(")
    entr_cx_1.insert(END, vvedennyi_inf_slovo_1_mew)
    entr_cx_1.insert(END, ")")
    entr_cx_1.insert(END, " = ")
    entr_cx_1.insert(END, new)
    entr_cx_1.configure(width = len(vvedennyi_polinom_mew) + len(vvedennyi_inf_slovo_1_mew) + len(new) + 15)

    entr_cx_2.delete(0, END)
    entr_cx_2.insert(0, "(")
    entr_cx_2.insert(END, vvedennyi_polinom_mew)
    entr_cx_2.insert(END, ")")
    entr_cx_2.insert(END, " * ")
    entr_cx_2.insert(END, "(")
    entr_cx_2.insert(END, vvedennyi_inf_slovo_2_mew)
    entr_cx_2.insert(END, ")")
    entr_cx_2.insert(END, " = ")
    entr_cx_2.insert(END, new1)
    entr_cx_2.configure(width=len(vvedennyi_polinom_mew) + len(vvedennyi_inf_slovo_2_mew) + len(new1) + 15)

    entr_cx_3.delete(0, END)
    entr_cx_3.insert(0, "(")
    entr_cx_3.insert(END, vvedennyi_polinom_mew)
    entr_cx_3.insert(END, ")")
    entr_cx_3.insert(END, " * ")
    entr_cx_3.insert(END, "(")
    entr_cx_3.insert(END, vvedennyi_inf_slovo_3_mew)
    entr_cx_3.insert(END, ")")
    entr_cx_3.insert(END, " = ")
    entr_cx_3.insert(END, new2)
    entr_cx_3.configure(width=len(vvedennyi_polinom_mew) + len(vvedennyi_inf_slovo_3_mew) + len(new2) + 15)


but_2_sp_1 = Button(frame4, text="Закодировать", command = X_umbojenie) # кнопка "Закодировать"
but_2_sp_1.grid(column=1, row = 5, sticky="w")


def decoding_search_miss():
    V1 = mistake(umnoj)[0]
    V2 = mistake(umnoj1)[0]
    V3 = mistake(umnoj2)[0]
    print(V1)
    entr_dec_v1.delete(0,END)
    entr_dec_v1.insert(0, V1)

    entr_dec_v2.delete(0, END)
    entr_dec_v2.insert(0, V2)

    entr_dec_v3.delete(0, END)
    entr_dec_v3.insert(0, V3)
    V_list = []
    V_list.append(V1)
    V_list.append(V2)
    V_list.append(V3)


    ex = vvedennyi_polinom_mew[:4]
    gx = vvedennyi_polinom_mew
    y = 0
    for i in range(len(V_list)):
        V_list_str = perevod(V_list[i]) # создаю список слов с ошибкой в виде многочлена
        Vx = " ".join(map(str, V_list_str))
        Sx = coding(ex, gx)[0]
        print(Vx, "Vx")
        print(gx, "gx")
        S__x = coding(Vx, gx)[0]
        print(Sx," Sx")
        print(S__x, " S'x")
        #умножаем S__x на х, т.е. каждому элементу прибаляем 1 степень, пока старшая не будет равна степени ex

        print(S__x, "то что домножаем на x")
        mnoj_1_0 = conventor(S__x)[0]
        ex_1_0 = conventor(ex)[0]
        chetchik_i = 0
        # 3 пункт
        if ex != S__x:
            while len(mnoj_1_0) < len(ex_1_0):
                mnoj_1_0.append(0)
                chetchik_i +=1
            print(mnoj_1_0, " умноженное на х i раз ")
            print(chetchik_i, "= i ")
            print(n)
            # 4 пункт
            step = int(n) - int(chetchik_i)
            Xni = list('1')
            t = 0
            print(step)
            while t < step:
                Xni.append('0')
                t+=1
            for i in range(len(Xni)):
                Xni[i] = int(Xni[i])
            print(Xni)

            Xni_ex = mnoj_1_0
            for i in range(len(Xni)-1):
                Xni_ex.append(0)
            print(Xni_ex)
            Xn_1 = list('1')
            r = 0

            while r < n:
                Xn_1.append('0')
                r += 1
            Xn_1[len(Xn_1)-1] = '1'
            for i in range(len(Xn_1)):
                Xn_1[i] = int(Xn_1[i])
            print(Xn_1)
            Xni_ex_x = perevod(Xni_ex)  # создаю делимое в виде многочлена
            Xni_ex__x = " ".join(map(str, Xni_ex_x))
            Xn_1_x = perevod(Xn_1)  # создаю делтель в виде многочлена
            Xn_1__x = " ".join(map(str, Xn_1_x))
            e__x = coding(Xni_ex__x, Xn_1__x)[0]
            print(e__x, " = e'x ")
        # пропуск 3 и 4 пунктов если S__x = ex
        else:
            e__x = ex # ОШИБКА В ВИДЕ МНОГОЧЛЕНА
            print(e__x, " e'x ")
        # 5 пункт

        Vx_1_0 = conventor(Vx)[0] # ЗАКОДИРОВАННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ С ОШИБКОЙ В ДВОИЧНОМ ВИДЕ
        e__x_1_0 = conventor(e__x)[0] # ОШИБКА В ДВОИЧНОМ ВИДЕ
        while len(e__x_1_0) < len(Vx_1_0):
            e__x_1_0.insert(0,0)
        c__x = [] # ИСПРАВЛЕННАЯ ЗАКОДИРОВАННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ В ДВОИЧНОЙ СИСТЕМЕ
        for i in range(len(Vx_1_0)):
            c__x.append(Vx_1_0[i] ^ e__x_1_0[i])

        c__x_x = perevod(c__x)
        c__x_str = " ".join(map(str, c__x_x))  # c'x строка целая"

        i__x = coding(c__x_str, gx)[1]
        print(i__x, " i-е информационное слово")
        print(i, "000000000000000")
        if y == 0:
            Lbl_ix_1.configure(text="")
            Lbl_ix_1.configure(text = i__x)
            entr_V1_.delete(0,END)
            entr_V1_.insert(END, "ex = " + ex)
            entr_V1_.insert(END, "; e'x = " + e__x)
            entr_V1_.insert(END, "; Sx = " + Sx)
            entr_V1_.insert(END, "; S'x =" + S__x)
            entr_V1_.insert(END, "; c'x=" + c__x_str)
            y += 1
        elif y == 1:
            Lbl_ix_2.configure(text = "")
            Lbl_ix_2.configure(text = i__x)
            entr_V2_.delete(0, END)
            entr_V2_.insert(END, "ex = " + ex)
            entr_V2_.insert(END, "; e'x = " + e__x)
            entr_V2_.insert(END, "; Sx = " + Sx)
            entr_V2_.insert(END, "; S'x =" + S__x)
            entr_V2_.insert(END, "; c'x=" + c__x_str)
            y += 1
        elif y == 2:
            Lbl_ix_3.configure(text="")
            Lbl_ix_3.configure(text = i__x)
            entr_V3_.delete(0, END)
            entr_V3_.insert(END, "ex = " + ex)
            entr_V3_.insert(END, "; e'x = " + e__x)
            entr_V3_.insert(END, "; Sx = " + Sx)
            entr_V3_.insert(END, "; S'x =" + S__x)
            entr_V3_.insert(END, "; c'x=" + c__x_str)




lbl_dec = Label(frame5, text="Способ декодирования \n Мэдита", font=("Roboto", 20), bg= "white") #Способ декодирования Мэдита
lbl_dec.grid(column = 1, row = 0, sticky = "wn")

lbl_dec_1 = Label(frame5, text="C(x) = i(x)*g(x)",font = (12), bg= "white") #формула
lbl_dec_1.grid(column = 1, row = 1, sticky = "wn")

lbl_dec_v1 = Label(frame5, text="V1 = ", bg= "white") # V1 =
lbl_dec_v1.grid(column = 1, row = 2, sticky = "w")
entr_dec_v1 = Entry(frame5)
entr_dec_v1.grid(column = 1, row = 2, sticky = "w", padx = 50)

lbl_dec_v2 = Label(frame5, text="V2 = ", bg= "white") # V2 =
lbl_dec_v2.grid(column = 1, row = 3, sticky = "w")
entr_dec_v2 = Entry(frame5)
entr_dec_v2.grid(column = 1, row = 3, sticky = "w", padx = 50)

lbl_dec_v3 = Label(frame5, text="V3 = ", bg= "white") #V3 =
lbl_dec_v3.grid(column = 1, row = 4, sticky = "w")
entr_dec_v3 = Entry(frame5)
entr_dec_v3.grid(column = 1, row = 4, sticky = "w", padx = 50)

but_dec = Button(frame5, text="Внести ошибки", command = decoding_search_miss) # кнопка "Закодировать"
but_dec.grid(column=1, row = 5, sticky="w")

lbl_ix = Label(frame5, text="Декодированные информационные слова",font = 30,  bg= "white")
lbl_ix.grid(column = 1, row = 6, sticky = "we")

lbl_ix_1 = Label(frame5, text="i(x)1 = ", bg= "white") # i(x)1 =
lbl_ix_1.grid(column = 1, row = 7, sticky = "w")
Lbl_ix_1 = Label(frame5)
Lbl_ix_1.grid(column = 1, row = 7, sticky = "w", padx = 50)

lbl_ix_2 = Label(frame5, text="i(x)2 = ", bg= "white") # i(x)2 =
lbl_ix_2.grid(column = 1, row = 8, sticky = "w")
Lbl_ix_2 = Label(frame5)
Lbl_ix_2.grid(column = 1, row = 8, sticky = "w", padx = 50)

lbl_ix_3 = Label(frame5, text="i(x)3 = ", bg= "white") # i(x)3 =
lbl_ix_3.grid(column = 1, row = 9, sticky = "w")
Lbl_ix_3 = Label(frame5)
Lbl_ix_3.grid(column = 1, row = 9, sticky = "w", padx = 50)

lbl_V1_ = Label(frame5, text="V1: ", bg= "white") # Sx =
lbl_V1_.grid(column = 1, row = 10, sticky = "w")

entr_V1_ = Entry(frame5, width = 50) # Sx =
entr_V1_.grid(column = 1, row = 10, sticky = "w", padx = 50)

lbl_V2_ = Label(frame5, text="V2: ", bg= "white") # S__x =
lbl_V2_.grid(column = 1, row = 11, sticky = "w")

entr_V2_ = Entry(frame5, width = 50) # Sx =
entr_V2_.grid(column = 1, row = 11, sticky = "w", padx = 50)

lbl_V3_ = Label(frame5, text="V3: ", bg= "white") # ex =
lbl_V3_.grid(column = 1, row = 12, sticky = "w")

entr_V3_ = Entry(frame5, width = 50) # Sx =
entr_V3_.grid(column = 1, row = 12, sticky = "W",padx =50)


# откуда берём строку для функции calc():
#Полином: vvedennyi_polinom_mew
#информационное слово 1: vvedennyi_inf_slovo_1_mew
#информационное слово 2: vvedennyi_inf_slovo_2_mew
#информационное слово 3: vvedennyi_inf_slovo_3_mew


tk.mainloop()