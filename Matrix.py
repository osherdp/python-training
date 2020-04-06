""" in this program Matrix is a tuple of tuples and the internal tuples must be as long as the
external list is.data is the Matrix (tuple) received from the user, and this class has add, sub,
 mul, scalar_mul and division by scalar methods and non- mathemathic methods
 as repr, str, hash and eq."""


class Matrix:
    """A matrices calculator for basic math actions
        Attributes:
            data(tuple of tuples): a Matrix- each line is a tuple in the major tuple """

    def __init__(self, data):
        #  inits a Matrix from received data (type= tuple), throws error for non- tuple inputs.
        check_value = True
        if type(data) is tuple:
            for tup in data:
                if len(tup) != len(data) or type(tup) is not tuple:
                    check_value *= 0
        else:
            check_value *= 0
        if check_value:
            self.data = data
        else:
            raise ValueError("Invalid matrix")

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        """prints the matrix in a format that can be used for build another Matrix"""
        return f"Matrix({self.data})"

    # str returns the Matrix in the mathemathic format
    def __str__(self):
        matrix_in_lines = ""
        for i in range(len(self.data)):
            matrix_in_lines += (str(self.data[i]) + "\n")
        return matrix_in_lines

    # unity method creates a matrix of zeros with a diagonal of ones (unity is the Matrix's size)
    @staticmethod
    def unity(unit):
        major_list = [[1 if i == index else 0 for i in range(unit)] for index in range(unit)]
        sub_list = [tuple(lt) for lt in major_list]
        # converts list of lists to type Matrix. lt are the inside lists
        matrix_to_return = Matrix((tuple(sub_list)))
        return matrix_to_return

    # ones method returns a Matrix full of ones which sizes determined by "unit"
    @staticmethod
    def ones(unit):
        sub_list = [tuple(lt) for lt in [([1] * unit) for i in range(unit)]]
        # convert list of lists to type Matrix. lt are the inside lists
        matrix_to_return = Matrix((tuple(sub_list)))
        return matrix_to_return

    def __add__(self, other):
        """add a matrix to another one
            args: self.data (tuple)- A matrix
                other(tuple) -A matrix

            returns: return the new matrix (tuple)

             raises: syntaxerror if "other" isn't a matrix"""
        if type(other) is Matrix:
            answer = []
            for tup in range(len(self.data)):
                answer.append([])
                for num in range(len(self.data)):
                    answer[tup].append(self.data[tup][num] + other[tup][num])
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
            for tup in range(len(self.data)):
                answer.append([])
                for num in range(len(self.data)):
                    answer[tup].append(self.data[tup][num] - other[tup][num])
            sub_list = [tuple(ls) for ls in answer]
            # converts list of lists to type Matrix. ls are the inside lists
            return Matrix((tuple(sub_list)))
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
            raise SyntaxError("only  scalar division")

    def __mul__(self, other):
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
        if type(other) is Matrix:  # Matrix's multiplication --->
            answer = []  # will contain the answer as a list of lists.
            new_other = []
            # this loop convert "other" from Matrix type to a list of lists named "new_other".
            for line in range(len(self.data)):
                new_other.append([])
                answer.append([0] * len(self.data))  # ns starts as a list of lists full of zeros.
                for num in range(len(self.data)):
                    new_other[line].append(other[num][line])
            # this is the multiplication process->
            for tup in range(len(self.data)):
                for num in range(len(self.data)):
                    for i in range(len(self.data)):
                        answer[tup][num] += self.data[tup][i] * new_other[num][i]
#                here the program adds to the zero the summery of the multiplications of
#                any two numbers which their places in the matrices are fits by the matrices
#                multiplication rules.
            sub_list = [tuple(ls) for ls in answer]
            # convert answer to type Matrix. ls are the inside lists.
            return Matrix((tuple(sub_list)))

    def scalar_mul(self, other):
        """multiply a matrix by a scalar
                    args: self.data (tuple)- A matrix
                        other(int/float) -A scalar

                    returns: return the new matrix (tuple)

                     raises: Syntaxerror if "other" isn't a scalar"""
        answer = []
        for tup in range(len(self.data)):
            answer.append([])
            for num in range(len(self.data)):
                answer[tup].append(self.data[tup][num] * other)
        sub_list = [tuple(ls) for ls in answer]
        # convert ans to type Matrix. ls are the inside lists
        return Matrix((tuple(sub_list)))

    def __eq__(self, other):
        """checks if two matrices are equal
                    args: self.data (tuple)- A matrix
                        other- anything

                    returns: True/False """
        return self.data == other

    # let matrix instances to be a key in a dictionary.
    def __hash__(self):
        return hash(self.data)
