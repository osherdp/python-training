from Calculator import Calc
from tkinter import *


class CalcGui:

    def __init__(self):
        """
        initialization_method, sets the window of the gui,
        and the input box - the text box where the exercise is entered.
        """
        self._root = Tk()
        self._input_box = Entry(self._root)
        self._initialize_gui()

    def _initialize_gui(self):
        """
        Initializing the rest of the widgets for the gui and pack them on the root window.'
        :return:
        """
        main_label = Label(self._root, text="Enter a calculation:", height=2)
        main_label.grid(row=0, columnspan=4)

        self._input_box.grid(row=1, columnspan=4)
        self._root.bind('<Return>', lambda e: self._input_box_get_solution())
        self._add_buttons()
        self._root.mainloop()

    def _add_buttons(self):
        """
        Adding the buttons for the gui, the buttons are saved in a dictionary
        with their name as a key, and the location as a list [row, column].
        :return:
        """
        buttons_dict = {'C': [2, 0], "DEL": [2, 1], '^': [2, 2], '/': [2, 3],
                        '7': [3, 0], '8': [3, 1], '9': [3, 2], 'X': [3, 3],
                        '4': [4, 0], '5': [4, 1], '6': [4, 2], '-': [4, 3],
                        '1': [5, 0], '2': [5, 1], '3': [5, 2], '+': [5, 3],
                        "-/+": [6, 0], '0': [6, 1], '.': [6, 2], '=': [6, 3]}

        for button in buttons_dict:

            # Outside function so the buttons values will be saved when called the command.
            action = lambda x=button: self.configure_entry_text(x)

            new_button = Button(self._root, text=button, height=2, width=4, command=action)
            new_button.grid(row=buttons_dict[button][0], column=buttons_dict[button][1])

    def configure_entry_text(self, value):
        """
        This function controls the entry box (the text box), of which the exercise is entered.
        This function can add or delete (or both) the current value in the text box.
        That depends on the value that inserted.
        :param value: Can be a name of a button or the solution itself.
        :return:
        """
        current_text_len = len(self._input_box.get())

        # Solution (buttons with numbers are string).
        if type(value) == float:
            self._input_box.delete(0, current_text_len)
            self._input_box.insert(0, value)

        # Special buttons
        elif value == '=':
            self._input_box_get_solution()

        elif value == "C":
            self._input_box.delete(0, current_text_len)

        elif value == '-/+':
            self._input_box.insert(1, '-')

        elif value == 'X':
            self._input_box.insert(current_text_len, '*')

        elif value == "DEL":
            self._input_box.delete(current_text_len - 1, current_text_len)

        # Other buttons.
        else:
            self._input_box.insert(current_text_len, value)

    def _input_box_get_solution(self):
        """
        Gets the solution of the exercise in the self._input_box and enter it in the same _input_box.
        The function makes a new Calc object and uses its find_solution() function.
        """
        new_exercise = Calc(self._input_box.get())
        self.configure_entry_text(float(new_exercise.find_solution()))


def main():
    CalcGui()


if __name__ == '__main__':
    main()
