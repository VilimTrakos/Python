from tkinter import *
from tkinter.messagebox import *

class Calculator(Frame):
    def __init__(self, t):
        self.t = t
        super().__init__(self.t)

        self.t.title('Calculator')
        self.grid(rows=4, columns=4, padx=20, pady=20)

        self.start_interface()
        self.bindKeys()

    def start_interface(self):
        font = ('Calibri', 20, 'normal')

        self.a_val = StringVar('')
        self.a = Entry(self, font=font, textvariable=self.a_val)
        self.a.grid(row=1, column=1, columnspan=2)

        self.b_val = StringVar('')
        self.b = Entry(self, font=font, textvariable=self.b_val)
        self.b.grid(row=1, column=3, columnspan=2)

        self.button_plus = Button(self, text="+", command=lambda: self.calc('+'))
        self.button_plus.grid(row=2, column=1)

        self.button_minus = Button(self, text="-", command=lambda: self.calc('-'))
        self.button_minus.grid(row=2, column=2)

        self.button_mult = Button(self, text="*", command=lambda: self.calc('*'))
        self.button_mult.grid(row=2, column=3)

        self.button_div = Button(self, text="/", command=lambda: self.calc('/'))
        self.button_div.grid(row=2, column=4)

        self.output_text = StringVar()
        self.output = Label(self, textvariable=self.output_text, font=font)
        self.output.grid(row=3,column=1, columnspan=4)

    def bindKeys(self):
        print('foo')
        # self.t.bind('<Control_L>', self.plus)
        # self.t.bind('<Control_R>', self.minus)
        # self.t.bind('<Alt_L>', self.div)
        # self.t.bind('<Shift_L>', self.mult)

    # "https://pastebin.com/0vGT4BzY"

    def calc(self, operation):
        try:
            a = int(self.a_val.get())
            b = int(self.b_val.get())
            c = 0
            if operation == '+':
                c = a + b
            elif operation == '-':
               c = a - b
            elif operation == '*':
                c = a * b
            else:
                c =a / b

            self.output_text.set(str(c))
        except ValueError:
            showinfo('Error','To nije broj')
            print('To nije broj')
        except ZeroDivisionError:
            showinfo('Error','Ne mozes dijeliti s 0')
            print('Ne mozes dijeliti sa 0')

calc = Calculator(Tk())
mainloop()