import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор Любви')
window.geometry('350x350')
window.resizable(False, False)
window.config(cursor = "heart", bg="#DC143C")
button_add = tk.Button(window, text = '+', width=2, height=2, command=add, background="#8470FF")
button_add.place(x = 100, y = 150)
button_sub = tk.Button(window, text = '-', width=2, height=2, command=sub, background="#8470FF")
button_sub.place(x = 125, y = 150)
button_mul = tk.Button(window, text = '*', width=2, height=2, command=mul, background="#8470FF")
button_mul.place(x = 150, y = 150)
button_div = tk.Button(window, text = '/', width=2, height=2, command=div, background="#8470FF")
button_div.place(x = 175, y = 150)
number1_entry = tk.Entry(window, width=16, background="#ADD8E6")
number1_entry.place(x = 100, y = 50)
number2_entry = tk.Entry(window, width=16, background="#ADD8E6")
number2_entry.place(x = 100, y = 100)
answer_entry = tk.Entry(window, width=16, background="#ADD8E6")
answer_entry.place(x = 100, y = 250)
number1 = tk.Label(window, text = 'Введите первое число:', background="#FFB6C1")
number1.place(x = 85, y = 25)
number2 = tk.Label(window, text = 'Введите второе число:', background="#FFB6C1")
number2.place(x = 85, y = 75)
answer = tk.Label(window, text = 'Вот настолько сильно я тебя люблю:', background="#FFB6C1")
answer.place(x = 50, y = 225)
answer = tk.Label(window, text = 'И это малая часть моих чувств к тебе:)', background="#FFB6C1")
answer.place(x = 50, y = 275)

window.mainloop()