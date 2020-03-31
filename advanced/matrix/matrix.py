__author__ = 'Anat'

from pip._vendor.msgpack.fallback import xrange


class Matrix:
    def __init__(self, matrix_values):
        self.__matrix_values = matrix_values
        if not self.check_if_squar():
            print("matrix not squar")

    def check_if_squar(self):
        for x in xrange(len(self.__matrix_values)):
            if len(self.__matrix_values) != len(self.__matrix_values[x]):
                return False
        return True

    def return_values(self):
        if self.check_if_squar():
            return self.__matrix_values

    def add(self, matrix):
        if self.check_if_squar():
            try:
                if len(self.return_values()) == len(matrix.return_values()):
                    for x in xrange(len(self.__matrix_values)):
                        for y in xrange(len(self.__matrix_values[x])):
                            self.__matrix_values[x][y] += matrix.return_values()[x][y]
                else:
                    print("matrix's not the same size")
            except TypeError:
                print("second matrix not squar")

    def sub(self, matrix):
        if self.check_if_squar():
            try:
                if len(self.return_values()) == len(matrix.return_values()):
                    for x in xrange(len(self.__matrix_values)):
                        for y in xrange(len(self.__matrix_values[x])):
                            self.__matrix_values[x][y] -= matrix.return_values()[x][y]
                else:
                    print("matrix's not the same size")
            except TypeError:
                print("second matrix not squar")

    def mul_by_scalar(self, scalar):
        if self.check_if_squar():
            for x in xrange(len(self.__matrix_values)):
                for y in xrange(len(self.__matrix_values[x])):
                    self.__matrix_values[x][y] *= scalar

    def div_by_scalar(self, scalar):
        if self.check_if_squar():
            try:
                for x in xrange(len(self.__matrix_values)):
                    for y in xrange(len(self.__matrix_values[x])):
                        self.__matrix_values[x][y] /= scalar
            except ZeroDivisionError:
                print("cant divide by zero")

    def mul(self, matrix):
        if self.check_if_squar():
            try:
                if len(self.return_values()) == len(matrix.return_values()):
                    matrix_after_mul = Matrix.unity(len(self.__matrix_values))
                    for x in xrange(len(self.__matrix_values)):
                        matrix1_row = self.__matrix_values[x]
                        for y in xrange(len(self.__matrix_values)):
                            matrix2_column = self.return_column(matrix, y)
                            current_value = 0
                            for a in xrange(len(self.__matrix_values)):
                                current_value += matrix1_row[a] * matrix2_column[a]
                            matrix_after_mul.return_values()[x][y] = current_value
                    self.__matrix_values = matrix_after_mul.return_values()
                else:
                    print("matrix's not the same size")
            except TypeError:
                print("second matrix not squar")

    def return_column(self, matrix, column_num):
        column = []
        for x in xrange(len(matrix.return_values())):
            column.append(matrix.return_values()[x][column_num])
        return column

    def __str__(self):
        return 'Matrix {}'. \
            format(self.__matrix_values)

    def __repr__(self):
        matrix_repr = ""
        for x in xrange(len(self.__matrix_values)):
            for y in xrange(len(self.__matrix_values[x])):
                matrix_repr += str(self.__matrix_values[x][y]) + " "
            matrix_repr += "\n"
        return matrix_repr

    def unity(size):
        unity_matrix_values = []
        for x in xrange(size):
            unity_matrix_values += [[0]]
            for y in xrange(size - 1):
                unity_matrix_values[x] += [0]
        for x in xrange(size):
            for y in xrange(size):
                if y == x:
                    unity_matrix_values[x][y] = 1
        unity_matrix = Matrix(unity_matrix_values)
        return unity_matrix


    def ones(size):
        one_matrix_values = []
        for x in xrange(size):
            one_matrix_values += [[1]]
            for y in xrange(size - 1):
                one_matrix_values[x] += [1]
        one_matrix = Matrix(one_matrix_values)
        return one_matrix

    def comparison(self, matrix):
        if self.check_if_squar() & matrix.check_if_squar():
            if len(self.__matrix_values) == len(matrix.return_values()):
                for x in xrange(len(self.__matrix_values)):
                    for y in xrange(len(self.__matrix_values[x])):
                        if self.__matrix_values[x][y] != matrix.return_values()[x][y]:
                            return False
                return True
            else:
                print("martix's not same size")
