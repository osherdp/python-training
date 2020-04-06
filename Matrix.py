"""matrices calculator class."""


class Matrix:
    """A matrices calculator for basic math actions
        Attributes:
            data(tuple of tuples): a Matrix- each line is a tuple in the major tuple """

    def __init__(self, data):
        if type(data) is not tuple:
            raise ValueError("Invalid matrix")
        for line in data:
            if len(line) != len(data) or type(line) is not tuple:
                raise ValueError("Invalid matrix")
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        """prints the matrix in a format that can be used for build another Matrix"""
        return f"{self.__class__.__name__}({self.data})"

    def __str__(self):
        matrix_in_lines = ""
        for i in range(len(self.data)):
            matrix_in_lines += (str(self.data[i]) + "\n")
        return matrix_in_lines

    @staticmethod
    def unity(size):
        """ unity method creates a matrix of zeros with a diagonal of ones
        args: size(int)- the size of the matrix and lines.
        returns: a matrix full of 0 and 1's diagonal
        exceptions: ValueError for non-ints"""
        if type(size) is int:
            major_list = [[1 if i == index else 0 for i in range(size)] for index in range(size)]
            # converts list of lists to type Matrix. lt are the inside lists
            return Matrix((tuple([tuple(lt) for lt in major_list])))
        else:
            raise ValueError("size must be an integer")

    @staticmethod
    def ones(size):
        """ones method returns a Matrix full of ones whose size determined by size variable
        args: size(int)- the size of the matrix and the lines
        returns: a matrix full of ones
        exceptions: ValueError for non-ints"""
        if type(size) is int:
            sub_list = [tuple(lt) for lt in [([1] * size) for i in range(size)]]
            matrix_to_return = Matrix((tuple(sub_list)))
            return matrix_to_return
        else:
            raise ValueError("size must be an integer")

    def __add__(self, other):
        """add a matrix to another one
            args: self.data (tuple)- A matrix
                other(tuple) -A matrix

            returns: return the new matrix (tuple)

             raises: syntaxerror if "other" isn't a matrix"""
        if type(other) is Matrix:
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
        """subtracting a matrix from another
                    args: self.data (tuple)- A matrix
                        other(tuple) -A matrix

                    returns: return the new matrix (tuple)

                     raises: syntaxerror if "other" isn't a matrix"""
        if type(other) is Matrix:
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
        """divides a matrix by scalar
                    args: self.data (tuple)- A matrix
                        other(int/float) -A scalar

                    returns: return the new matrix (tuple)

                     raises: syntaxerror if "other" isn't a scalar"""
        if type(other) is float or int:  # the program doesnt support division by other Matrix
            return self.scalar_mul(1 / other)
        else:
            raise SyntaxError("only scalar division")

    def __mul__(self, other):
        """mul function decides which multiply method is needed for each call
        args: self.data(matrix)- the first factor
         other(int/float/matrix)- the second factor
         no returns
         exceptions: SyntaxError if other isn't a matrix or a scalar"""
        if type(other) is Matrix:
            return self.matrices_mul(other)
        elif type(other) is float or type(other) is int:
            return self.scalar_mul(other)
        else:
            raise SyntaxError("invalid input")

    def matrices_mul(self, other):
        """multiply a matrix by matrix
                    args: self.data (tuple)- A matrix
                        other(tuple) -A matrix
                    returns: return the new matrix (tuple)"""
        answer = []
        new_other = []
        # this loop convert "other" from Matrix type to a list of lists named "new_other".
        for line in range(len(self.data)):
            new_other.append([])
            answer.append([0] * len(self.data))
            for num in range(len(self.data)):
                new_other[line].append(other[num][line])
        # this is the multiplication process->
        for line in range(len(self.data)):
            for num in range(len(self.data)):
                for i in range(len(self.data)):
                    answer[line][num] += self.data[line][i] * new_other[num][i]
#                   here the program adds to the zero the summery of the multiplications of
#                   any two numbers which their places in the matrices are fits by the matrices
#                   multiplication rules.
        return Matrix((tuple([tuple(ls) for ls in answer])))

    def scalar_mul(self, other):
        """multiply a matrix by a scalar
                args: self.data (tuple)- A matrix
                    other(int/float) -A scalar
                returns: return the new matrix (tuple)"""
        answer = []
        for line in range(len(self.data)):
            answer.append([])
            for num in range(len(self.data)):
                answer[line].append(self.data[line][num] * other)
        return Matrix((tuple([tuple(ls) for ls in answer])))

    def __eq__(self, other):
        """checks if two matrices are equal
                    args: self.data (tuple)- A matrix
                        other- anything
                    returns: True/False """
        return self.data == other

    def __hash__(self):
        """let matrix instances to be a key in a dictionary."""
        return hash(self.data)
