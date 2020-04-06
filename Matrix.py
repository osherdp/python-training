# -*- coding: utf-8 -*-
__author__ = 'Yaron'
"""
Module Matrix
This module includes the Matrix class and a main method used for testing it
"""


class Matrix:
    """
    This class is used to produces matrices and conduct operations on them.
    The class only supports squared matrices
    The matrix supports addition, subtraction, multiplication and division
    by scalar and matrices multiplication.
    """
    def __init__(self, tuples):
        self.__tuples = tuples

    def __len__(self):
        return len(self.tuples)

    def __repr__(self):
        return 'Matrix({})'.format(self.tuples)

    def __str__(self):
        return str(self.tuples)

    @classmethod
    def unity(cls, length):
        """
        Creates unit matrix of size length*length
        """
        def similar_index(x, y):
            """
            returns 1 when indices x and y are same, otherwise returns 0
            """
            if x == y:
                return 1
            return 0
        tuples = tuple([tuple([similar_index(i, j)
                               for i in range(length)])
                        for j in range(length)])
        return Matrix(tuples)

    @classmethod
    def ones(cls, length):
        """
        Creates matrix of size length*length where all elements equal 1
        """
        tuples = tuple([tuple([1] * length)] * length)
        return Matrix(tuples)

    def __add__(self, other):
        tuples = tuple([tuple([self.tuples[i][j] + other.tuples[i][j]
                               for j in range(len(self))])
                        for i in range(len(self))])
        return Matrix(tuples)

    def __sub__(self, other):
        tuples = tuple([tuple([self.tuples[i][j] - other.tuples[i][j]
                               for j in range(len(self))])
                        for i in range(len(self))])
        return Matrix(tuples)

    def __truediv__(self, value):
        tuples = tuple([tuple([self.tuples[i][j] / value
                               for j in range(len(self))])
                        for i in range(len(self))])
        return Matrix(tuples)

    def __eq__(self, other):
        return self.tuples == other.tuples

    def __mul__(self, other):
        if type(other) in [int, float]:
            tuples = tuple([tuple([self.tuples[i][j] * other
                                   for j in range(len(self))])
                            for i in range(len(self))])
        elif type(other) is Matrix:
            tuples = tuple([tuple([sum([self.tuples[i][m] * other.tuples[m][j]
                                        for m in range(len(self))])
                                   for j in range(len(self))])
                            for i in range(len(self))])
        else:
            raise TypeError
        return Matrix(tuples)

    def __hash__(self):
        return hash(self.tuples)

    def __iter__(self):
        self.row_num = 0
        return self

    def __next__(self):
        if self.row_num < len(self):
            row = self.tuples[self.row_num]
            self.row_num += 1
            return row
        else:
            raise StopIteration

    @property
    def tuples(self):
        """
        Holds the representation of the matrix as a tuple of tuples
        """
        return self.__tuples


def main():
    """
    This is code solely used for testing of the Matrix class
    """
    a = Matrix(((1, 2), (2, 3)))
    b = Matrix.unity(2)
    c = Matrix.ones(2)
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('c = {}'.format(c))
    print('a-b = {}'.format(a - b))
    print('a/2 = {}'.format(a / 2))
    print(iter(b))
    for line in a:
        print(line)
    print('a*2 = {}'.format(a * 2))
    print('a*b = {}'.format(a * b))
    print('a*c = {}'.format(a * c))


if __name__ == '__main__':
    main()
