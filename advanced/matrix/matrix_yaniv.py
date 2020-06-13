import sys


class matrix:
    def __init__(self, matrix_tuple):
        self.matrix_value = matrix_tuple
        if not self.sqr_check():
            print("matrix should be (n*n)")
            exit()

    def sqr_check(self):

        # checks if matrix is n*n

        for i in self.matrix_value:
            if len(self.matrix_value) != len(i):
                return False
        return True

    def repr(self):
        return str(self.matrix_value)

    def get_tuple(self):
        return self.matrix_value

    def ones(self, length):
        ones_list = []
        inside_ones = []
        for i in range(0, length):
            inside_ones.append(1)
        for i in range(0, length):
            ones_list.append(tuple(inside_ones))
        self.matrix_value = tuple(ones_list)
        return self

    def unity(self, length):
        unity_list = []

        for j in range(0, length):
            sublist = []
            for i in range(0, length):
                sublist.append(0)
            sublist[j] = 1
            unity_list.append(tuple(sublist))
        self.matrix_value = tuple(unity_list)
        return self

    def multiply(self, x):

        a = list(self.matrix_value)
        b = list(x.get_tuple())

        matrix_after_multiply = []
        for i in a:
            i = list(i)
            matrix_vector = []
            for p in range(0, len(a), 1):
                m = 0
                num = 0
                for j in b:
                    j = list(j)
                    num = num + (i[m] * j[p])
                    m = m + 1
                matrix_vector.append(num)
            matrix_after_multiply.append(tuple(matrix_vector))
        return matrix(tuple(matrix_after_multiply))

    def __add__(self, x):
        a = list(self.matrix_value)
        b = list(x.get_tuple())

        matrix_after_addition = []
        for i in range(0, len(a), 1):
            vector_matrix = []
            for p in range(0, len(a[i]), 1):
                vector_matrix.append(a[i][p] + b[i][p])
            matrix_after_addition.append(tuple(vector_matrix))
        return matrix(tuple(matrix_after_addition))

    def __sub__(self, x):
        a = list(self.matrix_value)
        b = list(x.get_tuple())

        matrix_after_substraction = []
        for i in range(0, len(a), 1):
            vector_matrix = []
            for p in range(0, len(a[i]), 1):
                vector_matrix.append(a[i][p] - b[i][p])
            matrix_after_substraction.append(tuple(vector_matrix))
        return matrix(tuple(matrix_after_substraction))

    def multiply_scalar(self, x):
        a = list(self.matrix_value)
        b = int(x)

        matrix_after_multiply = []

        for i in a:
            vector_matrix = []
            for p in range(0, len(i), 1):
                vector_matrix.append(i[p] * x)
            matrix_after_multiply.append(tuple(vector_matrix))
        return matrix(tuple(matrix_after_multiply))

    def __truediv__(self, x):
        a = list(self.matrix_value)
        b = int(x)

        matrix_after_divide = []

        for i in a:
            vector_matrix = []
            for p in range(0, len(i), 1):
                vector_matrix.append(i[p] / b)
            matrix_after_divide.append(tuple(vector_matrix))
        return matrix(tuple(matrix_after_divide))

    @property
    def tuples(self):
        return self.matrix_value

    def __ne__(self, x):
        a = list(self.matrix_value)
        b = list(x.get_tuple())

        for i in range(0, len(a), 1):
            for p in range(0, len(a[i]), 1):
                if a[i][p] != b[i][p]:
                    return True

        return False

    def __eq__(self, x):
        a = list(self.matrix_value)
        b = list(x.get_tuple())

        for i in range(0, len(a), 1):
            for p in range(0, len(a[i]), 1):
                if a[i][p] != b[i][p]:
                    return False

        return True

    @property
    def line_by_line(self):

        a = list(self.matrix_value)
        for i in range(0, len(a), 1):
            print(a[i])

    def __mul__(self, other):
        print("hello")
        if isinstance(other, matrix):
            return self.multiply(other)
        else:
            return self.multiply_scalar(other)

    def __rmul__(self, other):
        return self * other

    def __hash__(self):
        return hash(repr(self.matrix_value))
