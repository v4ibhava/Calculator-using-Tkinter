from tkinter import *


def calculate(val):
    current_text = result['text']
    if val == '00':
        if current_text == '0':
            result.config(text='00')
        elif current_text and current_text[-1] == '0':
            result.config(text=current_text + val)
        else:
            result.config(text=current_text + '0')
    elif val == '.':
        if '.' not in current_text:
            result.config(text=current_text + val)
        else:
            result.config(text=current_text)
    else:
        result.config(text=current_text + str(val))
def clear():
    current_text = result['text']
    new_text = current_text[:-1]
    result.config(text=new_text)
def all_clear():
    global num1, num2, optr
    num1 = 0
    num2 = 0
    optr = ''
    result.config(text='0')

def get_operator(op):
    global num1, num2, optr
    num1 = float(result['text'])
    optr = op
    result.config(text='')

def show_result():
    global num1, num2, optr
    num2 = float(result['text'])
    if optr == '+':
        result.config(text=str(num1 + num2))
    elif optr == '-':
        result.config(text=str(num1 - num2))
    elif optr == '*':
        result.config(text=str(num1 * num2))
    elif optr == '%':
        result.config(text=str(num1 % num2))
    else:
        if num2 == 0:
            result.config(text='ERROR')
        else:
            result.config(text=str(round(num1 / num2, 6)))

root = Tk()
root.title('CALCULATOR')
root.geometry('201x336')
root.resizable(0, 0)
root.configure(background='grey')
result = Label(root, text='', bg='grey', fg='white')
result.grid(row=0, column=0, pady=(20, 10), columnspan=20, sticky='w')
result.config(font=('Verdana', 30))
cfont = ('Terminal', 14)
h = 2
w = 4

# Row

btn_ac = Button(root, text="AC",width=w,height=h,command=lambda : all_clear(),bg='Black',fg='white')
btn_ac.grid(row=1,column=0)
btn_ac.config(font=cfont)

btn_per = Button(root, text="%",width=w,height=h,command= lambda : get_operator('%'),bg='Black',fg='white')
btn_per.grid(row=1,column=1)
btn_per.config(font=cfont)

btn_clear = Button(root, text="C",width=w,height=h,bg='Black',fg='white',command = lambda :clear())
btn_clear.grid(row=1,column=2)
btn_clear.config(font=cfont)

btn_div = Button(root, text="/",width=w,height=h,command= lambda : get_operator('/'),bg='Black',fg='white')
btn_div.grid(row=1,column=3)
btn_div.config(font=cfont)

# Row 2

btn_7 = Button(root, text="7",width=w,height=h,command=lambda :calculate(7),bg='Black',fg='white')
btn_7.grid(row=2,column=0)
btn_7.config(font=cfont)

btn_8 = Button(root, text="8",width=w,height=h,command=lambda :calculate(8),bg='Black',fg='white')
btn_8.grid(row=2,column=1)
btn_8.config(font=cfont)

btn_9 = Button(root, text="9",width=w,height=h,command=lambda :calculate(9),bg='Black',fg='white')
btn_9.grid(row=2,column=2)
btn_9.config(font=cfont)

btn_x = Button(root, text="X",width=w,height=h,command= lambda : get_operator('*'),bg='Black',fg='white')
btn_x.grid(row=2,column=3)
btn_x.config(font=cfont)

# Row 3

btn_4 = Button(root, text="4",width=w,height=h,command=lambda :calculate(4),bg='Black',fg='white')
btn_4.grid(row=3,column=0)
btn_4.config(font=cfont)

btn_5 = Button(root, text="5",width=w,height=h,command=lambda :calculate(5),bg='Black',fg='white')
btn_5.grid(row=3,column=1)
btn_5.config(font=cfont)

btn_6 = Button(root, text="6",width=w,height=h,command=lambda :calculate(6),bg='Black',fg='white')
btn_6.grid(row=3,column=2)
btn_6.config(font=cfont)

btn_sub = Button(root, text="-",width=w,height=h,command= lambda : get_operator('-'),bg='Black',fg='white')
btn_sub.grid(row=3,column=3)
btn_sub.config(font=cfont)

# Row 4

btn_1 = Button(root, text="1",width=w,height=h,command=lambda :calculate(1),bg='Black',fg='white')
btn_1.grid(row=4,column=0)
btn_1.config(font=cfont)

btn_2 = Button(root, text="2",width=w,height=h,command=lambda :calculate(2),bg='Black',fg='white')
btn_2.grid(row=4,column=1)
btn_2.config(font=cfont)

btn_3 = Button(root, text="3",width=w,height=h,command=lambda :calculate(3),bg='Black',fg='white')
btn_3.grid(row=4,column=2)
btn_3.config(font=cfont)

btn_add = Button(root, text="+",width=w,height=h,command= lambda : get_operator('+'),bg='Black',fg='white')
btn_add.grid(row=4,column=3)
btn_add.config(font=cfont)

# Row 5

btn_00 = Button(root, text="00",width=w,height=h,command=lambda :calculate(00),bg='Black',fg='white')
btn_00.grid(row=5,column=0)
btn_00.config(font=cfont)

btn_0 = Button(root, text="0",width=w,height=h,command=lambda :calculate(0),bg='Black',fg='white')
btn_0.grid(row=5,column=1)
btn_0.config(font=cfont)

btn_dot = Button(root, text=".",width=w,height=h,command=lambda :calculate('.'),bg='Black',fg='white')
btn_dot.grid(row=5,column=2)
btn_dot.config(font=cfont)

btn_equal = Button(root, text="=",width=w,height=h,command=show_result,bg='#FFB534',fg='black')
btn_equal.grid(row=5,column=3)
btn_equal.config(font=cfont)

root.mainloop()
