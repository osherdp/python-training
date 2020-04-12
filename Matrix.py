"""Matrices calculator class.

The matrices calculator can be used to add, sub, multiplication (by scalars or matrices) and scalar
division. also you can compare matrices or using them as a dictionary key. the program only works
with squared matrices.

    Typical usage example:

    x = Matrix(((1,2,3),(4,5,6),(6,7,8)))
    y = Matrix.unity(3)
    new_matrix = x * y
    """


class Matrix:
    """A matrices calculator for basic math actions.

        Attributes:
            data(tuple of tuples): a Matrix- each line is a tuple in the major tuple.
    """

    def __init__(self, data):
        if type(data) is not tuple:
            raise ValueError("Invalid matrix- not a tuple")

        for line in data:
            if len(line) != len(data) or type(line) is not tuple:
                raise ValueError("Invalid matrix- lines must be tuples and as long as the matrix")

        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def __str__(self):
        matrix_in_lines = ""
        for i in range(len(self.data)):
            matrix_in_lines += (str(self.data[i]) + "\n")
        return matrix_in_lines

    @staticmethod
    def unity(size):
        """ Unity method creates a matrix of zeros with a diagonal of ones.

        Args:
            size(int)- the size of the matrix and lines.

        Returns:
            A matrix full of 0 and 1's diagonal.

        Exceptions:
            ValueError: for non-integers.
        """
        if type(size) is int:
            # major_list will append sub lists with zeros and one if the index= major index.
            major_list = [[1 if i == index else 0 for i in range(size)] for index in range(size)]
            # converts list of lists to type Matrix. lt are the inside lists
            return Matrix((tuple([tuple(lt) for lt in major_list])))
        else:
            raise ValueError("size must be an integer")

    @staticmethod
    def ones(size):
        """Ones method returns a Matrix full of ones whose size determined by size variable.

        Args:
            size(int)- the size of the matrix and the lines.

        Returns:
            A matrix full of ones.

        Exceptions:
            ValueError: for non-ints.
        """
        if type(size) is int:
            sub_list = [tuple(lt) for lt in [([1] * size) for i in range(size)]]
            matrix_to_return = Matrix((tuple(sub_list)))
            return matrix_to_return
        else:
            raise ValueError("size must be an integer")

    def __add__(self, other):
        if isinstance(other, Matrix):
            answer = []
            for line in range(len(self.data)):
                answer.append([])
                for num in range(len(self.data)):
                    answer[line].append(self.data[line][num] + other[line][num])
            sub_list = [tuple(ls) for ls in answer]
            # convert answer to type Matrix. ls are the inside lists
            return Matrix((tuple(sub_list)))
        else:
            raise SyntaxError("only matrix's can be added together")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            answer = []
            for line in range(len(self.data)):
                answer.append([])
                for num in range(len(self.data)):
                    answer[line].append(self.data[line][num] - other[line][num])
            # converts list of lists to type Matrix. ls are the inside lists
            return Matrix((tuple([tuple(ls) for ls in answer])))
        else:
            raise SyntaxError("only matrix's subscription")

    def __truediv__(self, other):
        if type(other) is int or float:  # the program doesnt support division by other Matrix
            return self.scalar_mul(1 / other)
        else:
            raise SyntaxError("only scalar division")

    def __mul__(self, other):
        """Mul function decides which multiply method is needed for each call.

            Args:
                self.data(matrix)- the first factor.
                other(number/matrix)- the second factor.

            no returns.

            Exceptions:
                SyntaxError if other isn't a matrix or a scalar.
            """
        if isinstance(other, Matrix):
            return self.matrices_mul(other)
        elif type(other) is float or type(other) is int:
            return self.scalar_mul(other)
        else:
            raise SyntaxError("invalid input")

    def matrices_mul(self, other):
        """Multiply a matrix by matrix.

            Args:
                self.data (tuple)- A matrix.
                other(tuple) -A matrix.

            Returns:
                Return the new matrix (tuple).
            """
        answer = []
        for line in range(len(self.data)):
            answer.append([0] * len(self.data))
            for num in range(len(self.data)):
                for i in range(len(self.data)):
                    answer[line][num] += self.data[line][i] * other[i][num]
        return Matrix((tuple([tuple(ls) for ls in answer])))

    def scalar_mul(self, other):
        """Multiply a matrix by a scalar/
            Args:
                self.data (tuple)- A matrix.
                other(number) -A scalar.

            Returns:
                return the new matrix (tuple).
            """
        answer = []
        for line in range(len(self.data)):
            answer.append([])
            for num in range(len(self.data)):
                answer[line].append(self.data[line][num] * other)
        return Matrix((tuple([tuple(ls) for ls in answer])))

    __rmul__ = __mul__

    def __eq__(self, other):
        return tuple(self.data) == tuple(other)

    def __hash__(self):
        return hash(self.data)
