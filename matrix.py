import functools


class Matrix:
    def __init__(self, a):
        self.__a = tuple(a)

    @property
    def tuples(self):
        return tuple(self.__a)

    def unity(num, scalar=1):
        tuple_list = []
        number_list = []
        for row in range(num):
            for col in range(num):   # מוסיף מספרים לnumber_list לפי מספר העמודות במטריצה
                if col == row:      # מוסיף סקאלר רק כשמספר השורה שווה למספר העמודה
                    number_list.append(scalar)
                else:
                    number_list.append(0)
            tuple_list.append(tuple(number_list))  # מוסיף tuple עם המספרים בכל שורה לtuple_list לפי מספר השורות במטריצה
            number_list.clear()    # מאפס את number_list
        return Matrix(tuple(tuple_list))

    def ones(num):
        tuple_list = []
        number_list = []
        for row in range(num):
            for col in range(num):
                number_list.append(1)    # מוסיף מספרים לnumber_list לפי מספר העמודות במטריצה
            tuple_list.append(tuple(number_list))   # מוסיף tuple עם המספרים בכל שורה לtuple_list לפי מספר השורות במטריצה
            number_list.clear()    # מאפס את number_list
        return Matrix(tuple(tuple_list))

    def __add__(self, other):
        tuple_list = []
        number_list = []
        num = len(self.__a)
        for row in range(num):   # עובר על השורות במטריצה
            for col in range(num):   # עובר על העמודות במטריצה
                number_list.append(self.tuples[row][col] + other.tuples[row][col])
            tuple_list.append(tuple(number_list))   # שומר tuple (שורות) של המטריצה המחוברת
            number_list.clear()
        return Matrix(tuple(tuple_list))

    def __sub__(self, other):
        tuple_list = []
        number_list = []
        num = len(self.tuples)
        for row in range(num):  # עובר על השורות במטריצה
            for col in range(num):   # עובר על העמודות במטריצה
                number_list.append(self.tuples[row][col] - other.tuples[row][col])
            tuple_list.append(tuple(number_list))   # שומר tuple (שורות) של המטריצה המחוסרת
            number_list.clear()
        return Matrix(tuple(tuple_list))

    def __mul__(self, other):
        if type(other) == int:
            other = Matrix.unity(len(self.__a), other)     # הופך int למטריצה
        matrix_list = []
        tuple_list = []
        number_list = []
        num = len(self.__a)
        for col_a in range(num):   # עובר על העמודות במטריצה הראשונה
            for row in range(num):  # עובר על השורות במטריצה הראשונה
                for col_b in range(num):   # עובר על העמודות במטריצה השנייה
                    number_list.append(self.tuples[row][col_a] * other.tuples[col_a][col_b])
                tuple_list.append(tuple(number_list))  # שומר tuple (שורות) של המטריצה המוכפלת
                number_list.clear()
            matrix_list.append(Matrix(tuple_list))   # שומר את המטריצות המוכפלות
            tuple_list.clear()
        return functools.reduce(lambda x, y: x + y, matrix_list)   # מחבר את המטריצות המוכפלות

    def __truediv__(self, other):
        if type(other) == int:
            other = Matrix.unity(len(self.__a), other)    # הופך int למטריצה
        matrix_list = []
        tuple_list = []
        number_list = []
        num = len(self.__a)
        for col_a in range(num):  # עובר על העמודות במטריצה הראשונה
            for row in range(num):  # עובר על השורות במטריצה הראשונה
                for col_b in range(num):   # עובר על העמודות במטריצה השנייה
                    try:
                        number_list.append(self.tuples[row][col_a] / other.tuples[col_a][col_b])
                    except ZeroDivisionError:
                        number_list.append(0)
                tuple_list.append(tuple(number_list))   # שומר tuple (שורות) של המטריצה המחולקת
                number_list.clear()
            matrix_list.append(Matrix(tuple_list))   # שומר את המטריצות המחולקת
            tuple_list.clear()
        return functools.reduce(lambda x, y: x + y, matrix_list)   # מחבר את המטריצות המוכפלות

    def __eq__(self, other):
        num = len(self.__a)
        for row in range(num):  # עובר על השורות במטריצה
            for col in range(num):   # עובר על העמודות במטריצה
                if self.tuples[row][col] != other.tuples[row][col]:
                    return False
        return True

    def __iter__(self):
        return iter(self.__a)

    def __hash__(self):
        return hash(self.__a)

    def __str__(self):
        return "{}".format(self.tuples)

    def __repr__(self):
        return "{}".format(self.__a)
