from tkinter import *
from tkinter import messagebox
from code import *
from decode import *
import re


root = Tk()



def code():
    try:
        global file
        file = cc_entry.get()
        expression = cc1_entry.get()
        if function3(expression) == True:
            summators = int(expression)
            g = []
            m = []
            expression = cc2_entry.get()
            i = function2(file)
            if function4(expression) == True:
                while expression != '':
                    regexp = r'(\d+)'
                    match = re.search(regexp, expression)
                    if expression.find(" ") != -1:
                        m.append(expression[:expression.find(" ")])
                        expression = expression[expression.find(" ") + 1:]
                    else:
                        regexp = r"(\d+)"
                        a = re.search(regexp, expression)
                        m.append(a[0])
                        expression = ''
                for j in range(len(m)):
                    t = list(m[j])
                    g.append(t)
            else:
                messagebox.showerror('error', 'Something went wrong!')
            code_word = polinom(g, file)
            txt_1 = "".join(map(str, code_word))
            lbl_code(txt_1)
            fi1e = perform_viterbi_decoding(txt_1)

    except:
        messagebox.showerror('error', 'Something went wrong!')

def decode():
    try:
        lbl_decode(file)
    except:
        messagebox.showerror('error', 'Something went wrong!')

def lbl_code(word):
    lbl3["text"] = word

def lbl_decode(word):
    lbl4["text"] = word

root.title("Кодировщик")
root.geometry('400x200')

lbl=Label(root, text="Слово:", fg="#000000", width = 30)
lbl.grid(row=0, column = 0, columnspan=2)
lbl1=Label(root, text="Kол-во сумматоров:", fg="#000000")
lbl1.grid(row=1, column = 0, columnspan=2)
lbl2=Label(root, text="Позиции сумматоров:", fg="#000000", width = 30)
lbl2.grid(row=2, column = 0, columnspan=2)
lbl3=Label(root, text="", font=("Times New Roman", 8), fg="#000000", width = 50)
lbl3.grid(row=5, column = 0, columnspan=6)
lbl4=Label(root, text="", fg="#000000", width = 50)
lbl4.grid(row=7, column = 0, columnspan=6)

cc_entry = Entry(root, width = 38)
cc_entry.grid(row=0, column=3, columnspan=2)
cc1_entry = Entry(root, width = 38)
cc1_entry.grid(row=1, column=3, columnspan=2)
cc2_entry = Entry(root, width = 38)
cc2_entry.grid(row=2, column = 3, columnspan=2)

bttn = Button(root, text="Coging", width = 25, command = code)
bttn.grid(row=4, column = 0, columnspan=5)
bttn1 = Button(root, text="Decoding", command =decode, width = 25)
bttn1.grid(row=6, column = 0, columnspan=5)


root.mainloop()