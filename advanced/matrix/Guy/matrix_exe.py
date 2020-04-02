class Matrix(object):
    def __init__(self, list_tuple):
        self.__tuple = list_tuple
        self.__size = len(list_tuple)

    def ones(length):
        base = (1,)
        m_tuple = ((base * length),) * length
        return Matrix(m_tuple)

    def unity(length):
        b = ((1,) + (0,) * (length - 1)),
        zero = (0,)
        one = (1,)
        for i in range(1, length):
            c = (zero * i + one + zero * (length - i - 1)),
            b = b + c
        return Matrix(b)

    def tuples(self):
        return self.__tuple

    def __str__(self):
        return '{}'.format(self.__tuple)

    def __repr__(self):
        return 'Matrix({})'.format(self.__tuple)

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        if self.__size != other.__size:
            # raise IndexError
            return "Error - Matrices with different length!"
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j == 0:
                        temp = (self.__tuple[i][j] + other.__tuple[i][j]),
                    else:
                        if j == self.__size - 1:
                            if i == 0:
                                a = (self.__tuple[i][j] + other.__tuple[i][j]),
                                matrix = temp + a + (),
                            else:
                                a = (self.__tuple[i][j] + other.__tuple[i][j]),
                                temp = temp + a + (),
                                matrix = matrix + temp
                        else:
                            a = (self.__tuple[i][j] + other.__tuple[i][j]),
                            temp = temp + a
        return Matrix(matrix)

    def __sub__(self, other):
        if self.__size != other.__size:
            # raise IndexError
            return "Error - Matrices with different length!"
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j == 0:
                        temp = (self.__tuple[i][j] - other.__tuple[i][j]),
                    else:
                        if j == self.__size - 1:
                            if i == 0:
                                a = (self.__tuple[i][j] - other.__tuple[i][j]),
                                matrix = temp + a + (),
                            else:
                                a = (self.__tuple[i][j] - other.__tuple[i][j]),
                                temp = temp + a + (),
                                matrix = matrix + temp
                        else:
                            a = (self.__tuple[i][j] - other.__tuple[i][j]),
                            temp = temp + a
        return Matrix(matrix)

    def __mul__(self, other):
        if type(self) == type(other):
            if self.__size != other.__size:
                # raise IndexError
                return "Error - Matrices with different length!"
            else:
                for i in range(0, self.__size):
                    for j in range(0, self.__size):
                        if j == 0:
                            a = 0
                            for k in range(self.__size):
                                a = a + self.__tuple[i][k] *\
                                    other.__tuple[k][j]
                            temp = a,
                        else:
                            if j == self.__size - 1:
                                if i == 0:
                                    a = 0
                                    for k in range(self.__size):
                                        a = a + self.__tuple[i][k] *\
                                            other.__tuple[k][j]
                                    a = a,
                                    matrix = temp + a + (),
                                else:
                                    a = 0
                                    for k in range(self.__size):
                                        a = a + self.__tuple[i][k] *\
                                            other.__tuple[k][j]
                                    a = a,
                                    temp = temp + a + (),
                                    matrix = matrix + temp
                            else:
                                a = 0
                                for k in range(self.__size):
                                    a = a + self.__tuple[i][k] *\
                                        other.__tuple[k][j]
                                a = a,
                                temp = temp + a
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j == 0:
                        temp = ((self.__tuple[i][j]) * other),
                    else:
                        if j == self.__size - 1:
                            if i == 0:
                                a = ((self.__tuple[i][j]) * other),
                                matrix = temp + a + (),
                            else:
                                a = ((self.__tuple[i][j]) * other),
                                temp = temp + a + (),
                                matrix = matrix + temp
                        else:
                            a = ((self.__tuple[i][j]) * other),
                            temp = temp + a
        return Matrix(matrix)

    def __truediv__(self, num):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if j == 0:
                    temp = ((self.__tuple[i][j]) / num),
                else:
                    if j == self.__size - 1:
                        if i == 0:
                            a = ((self.__tuple[i][j]) / num),
                            matrix = temp + a + (),
                        else:
                            a = ((self.__tuple[i][j]) / num),
                            temp = temp + a + (),
                            matrix = matrix + temp
                    else:
                        a = ((self.__tuple[i][j]) / num),
                        temp = temp + a
        return Matrix(matrix)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            if self.__size != other.__size:
                return False
            else:
                for i in range(0, self.__size):
                    for j in range(0, self.__size):
                        if self.__tuple[i][j] != other.__tuple[i][j]:
                            return False
                return True

    def __ne__(self, other):
        if type(self) != type(other):
            return True
        else:
            if self.__size != other.__size:
                return True
            else:
                for i in range(0, self.__size):
                    for j in range(0, self.__size):
                        if self.__tuple[i][j] != other.__tuple[i][j]:
                            return True
                return False

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.__size:
            result = self.__tuple[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __hash__(self):
        return hash(self.__tuple)


def main():
    a = Matrix(((1, 2), (3, 4)))
    b = Matrix(((3, 5), (6, 8)))
    print(repr(a))
    print(a)
    print(repr(a.tuples()))
    print(repr(Matrix.unity(2)))
    print(repr(Matrix.unity(3)))
    print(repr(Matrix.ones(3)))
    print(repr(a * b))
    print(repr(a + Matrix.unity(2)))
    print(repr(a - b))
    print(repr(a * 10))
    print(repr(10 * a))
    print(repr(a / 10))
    print(repr(a != b))
    print(repr(a == b))
    for line in a:
        print(line)
    dictionary = {}
    dictionary[Matrix(((1, 1), (2, 2)))] = 1
    dictionary[Matrix(((1, 1), (2, 2)))] = 2
    dictionary[Matrix(((1, 1), (2, 3)))] = 3
    print(repr(dictionary))
    print('********************8*')

    print(dictionary.keys())
    print(dictionary.values())
    a = Matrix(((1, 2), (3, 4)))
    b = Matrix(((3, 5), (6, 8)))
    c = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    d = Matrix(((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)))
    e = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    f = Matrix(((10, 11, 12), (13, 14, 15), (16, 17, 18)))
    g = Matrix(((17, 18, 19, 20), (21, 22, 23, 24), (25, 26, 27, 28),
                (29, 30, 31, 32)))
    print(a == 5)
    print(a != 5)
    print(5 == c)
    print(a == a)
    print(a == b)
    print(b == a)
    print(c != a)
    print(a + a)
    print(a * b)
    print(e * f)
    print(d * g)
    print(g * d)
    for item in g:
        print(item)
    print(hash(a))
    print(hash(b))
    print(hash(Matrix(((1, 1), (2, 2)))))
    print(hash(Matrix(((1, 2), (3, 4)))))
    print(d * a)


if __name__ == '__main__':
    main()
