"""
Matrix exercise, Daniel Prince - unity training
"""


class Matrix:

    def __init__(self, data):
        """
        initializes the entered matrices and makes sure it is n x n
        """
        self.data = data
        # Check if n x n
        for tup in self.data:
            if len(self.data) != len(tup):
                raise ValueError("not a valid matrix. (not nXn)")
            else:
                continue

    def __str__(self):
        """display just the actual value of the instance

        Returns: the main outside tuple
        """
        return str(self.data)

    def __repr__(self):
        """display the instance of the class as is.

        Returns: a readable form of the matrix
        """
        return "Matrix({})".format(self.data)

    def __iter__(self):
        """ Allow iteration over a matrix instance

        Returns: the iterable version of the matrix

        """
        return iter(self.data)

    def __add__(self, other):
        """ Adds two matrices together.

        Args: the first matrix (self)
            other: the second matrix

        Returns: a new Class-type final addition result matrix.

        """
        if len(self.data) == len(other.data):
            post_add_list = []
            for tupA, tupB in zip(self.data, other.data):

                for numA, numB in zip(tupA, tupB):
                    post_add_list.append(numA + numB)

            return Matrix(tuple(splitting(post_add_list, len(self.data))))

        else:
            print("cannot perform addition on unequal matrix length")

    def __sub__(self, other):
        """ Subtracts two matrices one from the other.

        Args: first matrix (self)
            other: second matrix

        Returns: a new Class-type final subtraction result matrix.

        """
        if len(self.data) == len(other.data):
            post_sub_list = []
            for tupA, tupB in zip(self.data, other.data):

                for numA, numB in zip(tupA, tupB):
                    post_sub_list.append(numA - numB)

            return Matrix(tuple(splitting(post_sub_list, len(self.data))))

        else:
            print("cannot perform subtraction on unequal matrix length")

    def __mul__(self, other):
        """ Multiply two matrices or a matrix by a scalar

        Args: original matrix (self)
            other: a number or a second matrix

        Returns: a new Class-type final multiplication result matrix.

        """
        new_list = []
        if type(other) == Matrix:
            if len(self.data) == len(other.data):
                post_addition = []
                # Inverting the second matrix
                inverted_matrix = [] * len(self.data)
                for i in range(len(self.data)):

                    for tup in other.data:
                        inverted_matrix.append(tup[i])

                for t in self.data:
                    for l in splitting(inverted_matrix, len(self.data)):
                        for num, i2 in zip(l, range(len(self.data))):
                            post_addition.append(num * t[i2])

                for number1, number2 in zip(post_addition[::2],
                                            post_addition[1::2]):
                    new_list.append(number1 + number2)

            else:
                print("cannot perform multiplication on uneven matrices")

        else:
            for tup in self.data:
                for num in tup:
                    new_list.append(num * other)

        return Matrix(tuple(splitting(new_list, len(self.data))))

    def __floordiv__(self, other):
        """ Divide a matrix by a scalar

        Args: the matrix (self)
            other: a scalar to divide by

        Returns: a new class-type matrix final division result matrix

        """
        new_list = []
        if type(other) != Matrix:
            for tup in self.data:
                for num in tup:
                    new_list.append(num / other)

            return Matrix(tuple(splitting(new_list, len(self.data))))

        else:
            print("cannot divide matrix by matrix")

    def __eq__(self, other):
        """ compare instances of the class (==)

        Args: first matrix
            other: second matrix

        Returns: True/False

        """
        if type(other) == Matrix:
            if self.data == other.data:
                return True
            else:
                return False

        else:
            print("cannot check equivalency of type matrix and type int. ")

    def __ne__(self, other):
        """ compare instances of the class (!=)

        Args: first matrix
            other: second matrix

        Returns: True/False

        """
        if type(other) == Matrix:
            if self.data != other.data:
                return True
            else:
                return False

        else:
            print("cannot check equivalency of type matrix and type int. ")

    def __hash__(self):
        """ Make dict keys a hash

        Returns: the hashed tuple

        """
        return hash(self.data)

    @staticmethod
    def unity(num):
        """ Display tuple of tuples with 1 & 0
        so that the ones create a diagonal if seen as a square.

        Args:
            num: the amount of ones the user wants

        Returns: the final tuple, as a Matrix type

        """
        post_unity_list = []
        post_tup = []
        for i in range(num):
            set_list = [0] * num
            post_unity_list.append(set_list)
            post_unity_list[i][i] = 1

        # Tuple conversion:
        for l in post_unity_list:
            post_tup.append(tuple(l))

        return Matrix(tuple(post_tup))

    @staticmethod
    def ones(num):
        """ Display a tuple of tuples filled with ones.

        Args:
            num: the amount of tuples the user wants

        Returns: the final tuple, as a Matrix type

        """
        ones_tup = []
        ones_list = [[1] * num] * num

        # Tuple conversion:
        for l in ones_list:
            ones_tup.append(tuple(l))

        return Matrix(tuple(ones_tup))

    @property
    def tuples(self):
        """display the instance as tuple

        Returns: the raw tuple

        """
        return self.data

    # END OF CLASS --------------


def splitting(a_list, slice_number):
    """ Split a list into smaller lists and convert them to tuples.

    Args:
        a_list: the original unsliced list
        slice_number: the amount of small lists post slicing

    Returns: the final list of smaller tuples

    """
    inverted_list = [tuple(a_list[i * len(a_list) // slice_number:
                                  (i + 1) * len(a_list) // slice_number])
                     for i in range(slice_number)]
    return inverted_list
