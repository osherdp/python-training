"""Matrix exercise, Daniel Prince - unity training."""


class Matrix:
    """Perform all sorts of matrix operations."""

    def __init__(self, data):
        self.data = data
        # Check if n x n
        for tup in self.data:
            if len(self.data) != len(tup):
                raise ValueError("not a valid matrix. (not nXn)")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return '{self.__class__.__name__}({self.data})'.format(self=self)

    def __iter__(self):
        return iter(self.data)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __add__(self, other):
        """Adds 2 matrices."""

        if isinstance(other, Matrix):
            if len(self.data) == len(other.data):
                post_add_list = [self.data[row_i][column_i]
                                 + other.data[row_i][column_i]
                                 for row_i in range(len(self.data))
                                 for column_i in range(len(other.data))]
                return Matrix(tuple(splitting(post_add_list, len(self.data))))

            else:
                print("matrices must be equal length")

        else:
            print("cannot add a scalar")

    def __sub__(self, other):
        """Subtracts 2 matrices."""

        if isinstance(other, Matrix):
            if len(self.data) == len(other.data):
                post_sub_list = [self.data[row_i][column_i]
                                 - other.data[row_i][column_i]
                                 for row_i in range(len(self.data))
                                 for column_i in range(len(other.data))]
                return Matrix(tuple(splitting(post_sub_list, len(self.data))))

            else:
                print("matrices must be equal length")

        else:
            print("cannot subtract from a / a scalar")

    def __mul__(self, other):
        """Multiplies matrix by scalar/matrix."""

        if isinstance(other, Matrix):
            if len(self.data) == len(other.data):
                # Converting the second matrix to columns
                column_matrix = [tup[index] for index in range(len(self.data))
                                 for tup in other.data]
                split_column_matrix = splitting(column_matrix, len(self.data))
                post_mul = []
                for tup in self.data:
                    for split_list in split_column_matrix:
                        for num, index in \
                                zip(split_list, range(len(self.data))):
                            post_mul.append(num * tup[index])
                split_mul = splitting(post_mul,
                                      len(self.data) * len(self.data))
                added = [sum(tuples) for tuples in split_mul]
                final_mtx = splitting(added, len(self.data))
                return Matrix(tuple(final_mtx))
            else:
                print("cannot multiply different dimension matrices")

        else:
            final_mtx = [num * other for tup in self.data for num in tup]
            return Matrix(tuple(splitting(final_mtx, len(self.data))))

    def __truediv__(self, other):
        """Divide matrix by scalar."""

        if not isinstance(other, Matrix):
            divided_mtx = [num / other for tup in self.data for num in tup]
            return Matrix(tuple(splitting(divided_mtx, len(self.data))))

        else:
            print("cannot divide matrix by matrix")

    @staticmethod
    def unity(num):
        """Display tuple of tuples with 1 & 0
        so that the ones create a diagonal if seen as a square.

            Args:
                num: the amount of ones the user wants

            Returns: the final tuple, as a Matrix type
        """

        unity_list = [0 for _ in range(num * num)]
        unity_list[::num + 1] = [1 for _ in unity_list[::num + 1]]
        return Matrix(tuple(splitting(unity_list, num)))

    @staticmethod
    def ones(num):
        """Display a tuple of tuples filled with ones.

            Args:
                num: the amount of tuples the user wants

            Returns: the final tuple, as a Matrix type
        """

        ones_list = [1 for _ in range(num * num)]
        return Matrix(tuple(splitting(ones_list, num)))

    @property
    def tuples(self):
        """Display the instance as tuple.

            Returns: the raw tuple
        """

        return self.data

    # END OF CLASS --------------


def splitting(a_list, slice_number):
    """Split a list into smaller lists and convert them to tuples.

        Args:
            a_list: the original unsliced list
            slice_number: the amount of small lists post slicing

        Returns: the final list of smaller tuples
    """

    inverted_list = [tuple(a_list[i * len(a_list) // slice_number:
                                  (i + 1) * len(a_list) // slice_number])
                     for i in range(slice_number)]
    return inverted_list
