import functools


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

        self.check_value(self._matrix)

    @staticmethod
    def check_value(matrix_value):
        """
        Check if the input is according to the format of squared tuple, for example: ((a, b), (c, d)).
        Raise syntax error otherwise.
        """
        is_ok = True
        len_mat = len(matrix_value)

        for tup in matrix_value:
            if len(tup) != len_mat:
                is_ok = False

        if not is_ok:
            raise SyntaxError("Syntax error on defying the Matrix."
                              " Needs to be a 'squared tuple'. " + str(matrix_value))

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
        self.check_value(new_matrix)
        self._matrix = new_matrix

    @classmethod
    def ones(cls, len_tup):
        """
         Class method, make a new  Matrix object made of ones only, according to the len_tup inserted.
        In this format for example: Matrix.unity(3) = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
        :param len_tup: The length of the main tuple. (Amount of tuples in the Matrix).
        """
        # Input check.  TODO input check for every method.
        if len_tup < 1:
            raise ValueError("The length of a Matrix needs to be positive.")
        if type(len_tup) != int:
            raise TypeError("The length of  a Matrix object must be an integer number")
        mat = ()
        second_tup = ()
        for i in range(len_tup):
            second_tup += (1,)

        for j in range(len_tup):
            mat += (second_tup,)

        return Matrix(mat)

    def __mul__(self, other):
        """
        Method that implement a Matrix multiplication.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: New Matrix object which is the matrix multiplication result of self and other.
        """
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

            ans_mat += (second_tup, )

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

            opp_mat += (second_tup, )

        return Matrix(opp_mat)

    def __add__(self, other):
        """
        Method that implement a Matrix addition.
        :param self: The first Matrix object.
        :param other: The second Matrix object.
        :return: New Matrix object which is the matrix sum result of self and other.
        """
        mat_result = ()
        for i in range(len(self._matrix)):
            mat_result += (tuple(map((lambda x, y: x + y), self.tuples()[i], other.tuples()[i])),)

        return Matrix(mat_result)
def main():
    a = Matrix((1, 2), (3, 4))

    # mat2 = Matrix((1, ),)
    # mat3 = Matrix((1, 2, 3), (4, 5, 6), (7, 8, 9))
    # mat4 = Matrix((1, 2, 3, 4), (4, 5, 6, 7), (7, 8, 9, 10), (10, 11, 12, 13))
    # print(mat1)
    # print(mat2)
    # print(mat3)
    # print(mat4)
    # for i in range(1, 4):
    #     print(Matrix.unity(i))
    # mat1.set_matrix(((1, 1), (2, 2)))
    # print(mat1)
    # mat5 = Matrix.ones(3)
    # print(mat5)
    mat6 = Matrix((1, 2, 3), (4, 5, 6), (7, 8, 9))
    mat7 = Matrix((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(mat6 * mat7)

    print(mat6 + mat7)
    print(a + Matrix.unity(2))


if __name__ == '__main__':
    main()
