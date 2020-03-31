from typing import Dict


class Matrix:
    def __init__(self, *args):
        """
        Initialize method - Organize the Matrix checks the input as well.
        """
        # Remove unnecessary brackets. Like so: (((1, 2), (3, 4)),)
        if type(args[0][0]) == tuple:
            self._matrix = args[0]
        else:
            self._matrix = args

        self._check_input(self._matrix)

    @staticmethod
    def _check_input(matrix_value):
        """
        Check if the input is according to the format of squared tuple (n * n), for example: ((a, b), (c, d)).
        Checks if a b c d are integers or floats.
        Raise error otherwise.
        """
        format_is_ok = True
        value_is_ok = True
        len_mat = len(matrix_value)

        for tup in matrix_value:
            # Checks format (n * n matrix)
            if len(tup) != len_mat:
                format_is_ok = False

            for value in tup:
                # Checks the value of the tuples.
                if not (type(value) == int or type(value) == float):
                    value_is_ok = False

        if not format_is_ok:
            raise SyntaxError("Syntax error while defying the Matrix."
                              " Needs to be a 'squared tuple' (n * n Matrix). => " + str(matrix_value))
        if not value_is_ok:
            raise TypeError("TypeError error while defying the Matrix."
                            " All values must be float or integer numbers. => " + str(matrix_value))

    def __str__(self):
        """
        Returns a string value of the Matrix class. For print() function.
        """
        return str(self._matrix)

    def __repr__(self):
        """
        Returns representation of the matrix.
        """
        return "Matrix%s" % str(self._matrix)

    def __len__(self):
        """
        :return: The length of the matrix. (The order n of the squared Matrix).
        """
        return len(self._matrix)

    def __getitem__(self, item=None):
        """
        :param item: returns a specific item. Irrelevant in this case.
        :return: The matrix object itself.
        """
        return self._matrix

    def tuples(self):
        """
        Displays the matrix as a tuple.
        """
        return self._matrix

    @classmethod
    def unity(cls, len_tup):
        """
        Class method, make a new unity Matrix object according to the len_tup inserted.
        In this format, for example Matrix.unity(3): ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        :param len_tup: The length of the main tuple. (Amount of tuples in the Matrix).
        """
        if type(len_tup) != int:
            raise TypeError("The length of a unity Matrix has to be an integer number not '%s'."
                            % len_tup.__class__.__name__)
        if len_tup <= 0:
            raise ValueError("The length of a unity Matrix has to be a positive number. => " + str(len_tup))

        mat = ()
        second_tup = ()
        index = 0
        for tup in range(len_tup):
            for i in range(len_tup):
                if i == index:
                    second_tup += (1,)
                else:
                    second_tup += (0,)
            mat += (second_tup,)
            second_tup = ()
            index += 1

        return Matrix(mat)

    def set_matrix(self, new_matrix):
        """
        Set a new matrix value. Check the syntax first.
        An example of the wanted syntax  - mat1.set_matrix(((1, 1), (2, 2))).
        :param new_matrix: The wanted value.
        """
        self._check_input(new_matrix)
        self._matrix = new_matrix

    @classmethod
    def ones(cls, len_tup):
        """
         Class method, make a new  Matrix object made of ones only, according to the len_tup inserted.
        In this format for example: Matrix.ones(3) = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
        :param len_tup: The length of the main tuple. (Amount of tuples in the Matrix).
        """
        if type(len_tup) != int:
            raise TypeError("The length of a unity Matrix has to be an integer number not '%s'."
                            % len_tup.__class__.__name__)
        if len_tup <= 0:
            raise ValueError("The length of a unity Matrix has to be a positive number. => " + str(len_tup))

        mat = ()
        second_tup = ()
        for i in range(len_tup):
            second_tup += (1,)

        for j in range(len_tup):
            mat += (second_tup,)

        return Matrix(mat)

    def __mul__(self, other):
        """
        Method that implement a Matrix multiplication. In this format: self * other.
        :param self: The first Matrix object.
        :param other: A second object.
        :return: New Matrix object which is the matrix multiplication result of self and other.
        """
        # In this format: Matrix * scalar
        if type(other) == int or type(other) == float:
            return self._scalar_multiplication(other)

        if type(other) == Matrix:
            return self.matrix_multiplication(other)

        else:
            raise TypeError("Type error raised, can't multiply Matrix object by '%s' object."
                            % other.__class__.__name__)

    def __rmul__(self, other):
        """
        Method that implement a Matrix multiplication by scalar in this format: scalar * Matrix. (self * other)
        :param other: Int or float value.
        :return:
        """
        return self.__mul__(other)

    def _scalar_multiplication(self, scalar):
        """
        Method that implement a Matrix and scalar multiplication .
        :param self: The first Matrix object.
        :param scalar: The scalar. (Int or float object).
        :return: New Matrix object which is the matrix multiplication result of the Matrix object given and the scalar.
        """
        mat_result = ()
        for i in range(len(self._matrix)):
            mat_result += (tuple(map((lambda x: x * scalar), self.tuples()[i])),)

        return Matrix(mat_result)

    def matrix_multiplication(self, other):
        """
        Method that implement a Matrix multiplication.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: New Matrix object which is the matrix multiplication result of self and other.
        """
        if type(other) != Matrix:
            raise TypeError("Matrix multiplication have to be with 2 Matrix objects")

        # Changing the second Matrix so the rows and columns would switch.
        # This way implementing the multiplication formula it is more simple.
        other = other.opposite_matrix()

        mat_len = len(self._matrix)
        ans_mat = ()

        # col_ind refers to the index of a tuple in the first Matrix given.
        for mat1_ind in range(mat_len):
            second_tup = ()

            # row_ind refers to the index of a tuple in the second Matrix (The opposite one)).
            for mat2_ind in range(mat_len):
                # Adding the multiplication result of every value in the 2 tuples with the same index.
                second_tup += (sum(list(map((lambda x, y: x * y), self.tuples()[mat1_ind], other.tuples()[mat2_ind]))),)

            ans_mat += (second_tup,)

        return Matrix(ans_mat)

    def opposite_matrix(self):
        """
        Changing the columns with the rows in Matrix object.
        :param self: The Matrix object.
        :return: A opposite Matrix. for example opposite_matrix((1,2,3),(4,5,6),(7,8,9)) = ((1,4,7),(2,5,8),(3,6,9))
        """

        opp_mat = ()
        for index_in_tup in range(len(self._matrix)):
            second_tup = ()

            for tup_in_mat in range(len(self._matrix)):
                second_tup += (self.tuples()[tup_in_mat][index_in_tup],)

            opp_mat += (second_tup,)

        return Matrix(opp_mat)

    def __add__(self, other):
        """
        Method that implement a Matrix addition.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: New Matrix object which is the matrix sum result of self and other.
        """
        if type(other) != Matrix:
            raise TypeError("Type error, can't add a '%s' to a Matrix objects" % other.__class__.__name__)

        mat_result = ()
        for i in range(len(self._matrix)):
            mat_result += (tuple(map((lambda x, y: x + y), self.tuples()[i], other.tuples()[i])),)

        return Matrix(mat_result)

    def __sub__(self, other):
        """
        Method that implement a Matrix subtraction.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: New Matrix object which is the matrix subtraction result of other from self.
        """
        if type(other) != Matrix:
            raise TypeError("Type error, can't subtract '%s' from Matrix objects" % other.__class__.__name__)

        mat_result = ()
        for i in range(len(self._matrix)):
            mat_result += (tuple(map((lambda x, y: x - y), self.tuples()[i], other.tuples()[i])),)

        return Matrix(mat_result)

    def __truediv__(self, other):
        """
        Method that implement a Matrix division by scalar.
        :param self: The first Matrix object.
        :param other: Scalar (int or float object).
        :return: New Matrix object which is the Matrix division by scalar.
        """
        if type(other) != int and type(other) != float:
            raise TypeError("Type error raised, can't divide Matrix object by '%s' object." % other.__class__.__name__)

        scalar = 1 / other
        return self._scalar_multiplication(scalar)

    def __eq__(self, other):
        """
        Method that implement a Matrix comparision.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: Boolean value - if the Matrix object are identical.
        """
        if type(other) != Matrix:
            return False
        return self.tuples() == other.tuples()

    def __ne__(self, other):
        """
        Method that implement a Matrix inequality.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: Boolean value - if the Matrix object are *not* identical.
        """
        if type(other) != Matrix:
            return True

        return self.tuples() != other.tuples()

    def __iter__(self):
        return iter(self.tuples())

    def __hash__(self):
        return hash(self.tuples())


def main():

    a = Matrix((1, 2), (3, 4))
    b = Matrix((3, 5), (6, 8))

    print(repr(a))
    print(a)
    print(a.tuples())
    print(Matrix.unity(2))
    print(Matrix.unity(3))
    print(repr(a * b))
    print(a + Matrix.unity(2))
    print(a - b)
    print(a * 10)
    print(10 * a)
    print(a / 10)
    print(a / 10)
    print(a != b)
    print(a == b)
    for line in a:
        print(line)

    dictionary = {}
    dictionary[Matrix(((1, 1), (2, 2)))] = 1
    dictionary[Matrix(((1, 1), (2, 2)))] = 2
    dictionary[Matrix(((1, 1), (2, 3)))] = 3
    print(repr(dictionary))


if __name__ == '__main__':
    main()
