from tkinter import *


class Calc:
    def __init__(self):
        self.gui_user_input()

    @staticmethod
    def organize_input(string_calc):
        list_calc = []
        list_strong_op = ["*", "/", "^"]
        list_weak_op = ["-", "+"]

        for op in list_strong_op:
            try:
                index = string_calc.index(op)
                list_calc.append(float(string_calc[:index]))
                list_calc.append(op)
                list_calc.append(float(string_calc[index + 1:]))
            except ValueError:
                pass
        if not list_calc:
            for op in list_weak_op:
                try:
                    index = string_calc[1:].index(op) + 1
                    int(string_calc[index - 1])
                    list_calc.append(float(string_calc[:index]))
                    list_calc.append(op)
                    list_calc.append(float(string_calc[index + 1:]))
                except ValueError:
                    pass
        return list_calc

    @staticmethod
    def simple_calc(list_calc):
        num1 = list_calc[0]
        operator = list_calc[1]
        num2 = list_calc[2]

        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            return num1 / num2
        if operator == "^":
            return num1 ** num2

    @staticmethod
    def configure_entry_text(value, input_box):
        text = input_box.get()
        text_len = len(text)
        if type(value) == float:
            input_box.delete(0, text_len)
            input_box.insert(0, value)
        elif value == "C":
            input_box.delete(0, text_len)
        elif value == "DEL":
            input_box.delete(text_len - 1, text_len)
        else:
            input_box.insert(text_len, value)

    def is_this_solution(self, string_calc):
        for char in string_calc[1:]:
            if self.is_char_op(char):
                return False
        return True

    @staticmethod
    def is_char_op(char):
        op_lst = ["+", "-", "*", "/", "^"]
        if char in op_lst:
            return True
        return False

    def pulling_the_first_calc(self, string_calc, strong_op_index):
        flag = False
        first_index = strong_op_index
        last_index = strong_op_index

        while not flag:
            first_index -= 1
            if first_index == 0:
                flag = True
            elif self.is_char_op(string_calc[first_index]):
                first_index += 1
                flag = True

        flag = False
        while not flag:
            last_index += 1
            if last_index == len(string_calc) - 1:
                last_index += 1
                flag = True
            elif self.is_char_op(string_calc[last_index]) and not last_index == strong_op_index + 1:
                flag = True

        return string_calc[:first_index], string_calc[first_index:last_index], string_calc[last_index:]

    @staticmethod
    def index_strongest(string_calc):

        if "^" in string_calc:
            return string_calc.index("^")

        if "*" in string_calc or "/" in string_calc:
            try:
                multi_index = string_calc.index("*")
            except ValueError:
                multi_index = len(string_calc)
            try:
                divide_index = string_calc.index("/")
            except ValueError:
                divide_index = len(string_calc)

            return min(multi_index, divide_index)

        if "-" in string_calc or "+" in string_calc[1:]:
            try:
                plus_index = string_calc[1:].index("+") + 1
            except ValueError:
                plus_index = len(string_calc)
            try:
                minus_index = string_calc[1:].index("-") + 1
            except ValueError:
                minus_index = len(string_calc)

            return min(plus_index, minus_index)
    """ 
    def get_answer(self, string_calc, input_box):
        list_calc = self.organize_input(string_calc)
        solution = self.simple_calc(list_calc)
        self.configure_entry_text(solution, input_box)
        print(str(solution))
    """

    def get_answer(self, string_calc, input_box):
        if self.is_this_solution(string_calc):
            return self.configure_entry_text(float(string_calc), input_box)

        strong_op_index = self.index_strongest(string_calc)
        string_calc_tuple = self.pulling_the_first_calc(string_calc, strong_op_index)
        list_calc = self.organize_input(string_calc_tuple[1])
        return self.get_answer(string_calc_tuple[0] + str(self.simple_calc(list_calc)) + string_calc_tuple[2],
                               input_box)

    def gui_user_input(self):
        root = Tk()
        main_label = Label(root, text="Enter a calculation:", height=2)
        main_label.grid(row=0, columnspan=4)
        input_box = Entry(root)
        input_box.grid(row=1, columnspan=4)
        root.bind('<Return>', lambda e: self.get_answer(input_box.get(), input_box))
        bt1 = Button(root, text="1", height=2, width=4, command=lambda: self.configure_entry_text("1", input_box))
        bt2 = Button(root, text="2", height=2, width=4, command=lambda: self.configure_entry_text("2", input_box))
        bt3 = Button(root, text="3", height=2, width=4, command=lambda: self.configure_entry_text("3", input_box))
        bt4 = Button(root, text="4", height=2, width=4, command=lambda: self.configure_entry_text("4", input_box))
        bt5 = Button(root, text="5", height=2, width=4, command=lambda: self.configure_entry_text("5", input_box))
        bt6 = Button(root, text="6", height=2, width=4, command=lambda: self.configure_entry_text("6", input_box))
        bt7 = Button(root, text="7", height=2, width=4, command=lambda: self.configure_entry_text("7", input_box))
        bt8 = Button(root, text="8", height=2, width=4, command=lambda: self.configure_entry_text("8", input_box))
        bt9 = Button(root, text="9", height=2, width=4, command=lambda: self.configure_entry_text("9", input_box))
        bt0 = Button(root, text="0", height=2, width=4, command=lambda: self.configure_entry_text("0", input_box))

        btc = Button(root, text="C", height=2, width=4, command=lambda: self.configure_entry_text("C", input_box))
        bt_dot = Button(root, text=".", height=2, width=4, command=lambda: self.configure_entry_text(".", input_box))
        bt_sign = Button(root, text="-/+", height=2, width=4, command=lambda: self.configure_entry_text("-", input_box))
        bt_minus = Button(root, text="-", height=2, width=4, command=lambda: self.configure_entry_text("-", input_box))
        bt_plus = Button(root, text="+", height=2, width=4, command=lambda: self.configure_entry_text("+", input_box))
        bt_divide = Button(root, text="/", height=2, width=4, command=lambda: self.configure_entry_text("/", input_box))
        bt_multi = Button(root, text="X", height=2, width=4, command=lambda: self.configure_entry_text("*", input_box))
        bt_equals = Button(root, text="=", height=2, width=4, command=lambda: self.get_answer(input_box.get(), input_box))
        bt_power = Button(root, text="^", height=2, width=4, command=lambda: self.configure_entry_text("^", input_box))
        bt_square = Button(root, text="", height=2, width=4, command=lambda: self.configure_entry_text("??", input_box))
        bt_del = Button(root, text="DEL", height=2, width=4, command=lambda: self.configure_entry_text("DEL", input_box))

        btc.grid(row=2, column=0)
        bt_del.grid(row=2, column=1)
        bt_power.grid(row=2, column=2)
        bt_divide.grid(row=2, column=3)

        bt7.grid(row=3, column=0)
        bt8.grid(row=3, column=1)
        bt9.grid(row=3, column=2)
        bt_multi.grid(row=3, column=3)

        bt4.grid(row=4, column=0)
        bt5.grid(row=4, column=1)
        bt6.grid(row=4, column=2)
        bt_minus.grid(row=4, column=3)

        bt1.grid(row=5, column=0)
        bt2.grid(row=5, column=1)
        bt3.grid(row=5, column=2)
        bt_plus.grid(row=5, column=3)

        bt_sign.grid(row=6, column=0)
        bt0.grid(row=6, column=1)
        bt_dot.grid(row=6, column=2)
        bt_equals.grid(row=6, column=3)

        root.mainloop()


Calc()

