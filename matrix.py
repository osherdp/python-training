"""Matrix exercise."""


class Matrix:
    """Perform all sorts of matrix operations."""

    def __init__(self, data):
        self.data = data
        # Check if n x n
        for tuple_ in self.data:
            if len(self.data) != len(tuple_) or not\
                    all(isinstance(n, (int, float)) for n in
                        [val for self_tuple in self.data
                         for val in self_tuple]):
                raise ValueError("not a valid matrix.")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data})'

    def __iter__(self):
        return iter(self.data)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if isinstance(other, Matrix):
            n = len(self.data)
            if n == len(other.data):
                post_add_list = [self.data[row_i][column_i]
                                 + other.data[row_i][column_i]
                                 for row_i in range(n)
                                 for column_i in range(len(other.data))]
                return __class__(tuple(splitting(post_add_list, n)))

            # post_add = [[] for _ in range(len(self.data))]
            # for self_tup, other_tup, index in zip(self.data, other.data, range(len(self.data))):
            #     for num1, num2 in zip(self_tup, other_tup):
            #         post_add[index].append(num1 + num2)
            # final_mtx = tuple(tuple(x) for x in post_add)
            # return __class__(final_mtx)

            else:
                raise ValueError("matrices must be equal length")

        else:
            raise ValueError("cannot add a scalar")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            negative = other.__rmul__(-1)
            final = negative.__add__(self)
            return final

        else:
            raise ValueError("cannot subtract a scalar")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            n = len(self.data)
            if n == len(other.data):
                # Converting the second matrix to columns
                column_mtx = [[row[i] for row in other.data] for i in range(n)]
                # Multiplying the matrices
                temp_list = []
                post_mul = [[] for _ in range(n)]
                for tuple_, index in zip(self.data, range(n)):
                    for split_list in column_mtx:
                        for number, index_ in zip(split_list, range(n)):
                            temp_list.append(number * tuple_[index_])
                            if len(temp_list) >= n:
                                post_mul[index].append(sum(temp_list))
                                del temp_list[:]
                final_mtx = tuple(tuple(x) for x in post_mul)
                return __class__(final_mtx)

            else:
                print("cannot multiply different dimension matrices")

        else:
            return self.__rmul__(other)

    def __rmul__(self, other):
        final_mtx = [num * other for tup in self.data for num in tup]
        return __class__(tuple(splitting(final_mtx, len(self.data))))

    def __truediv__(self, other):
        if not isinstance(other, Matrix):
            return self.__mul__(1/other)

        else:
            print("cannot divide matrix by matrix")

    @staticmethod
    def unity(number):
        """Display tuple of tuples with 1 & 0.

        The ones create a diagonal if seen as a square.

        Args:
            number(int): the amount of ones the user wants

        Returns(Matrix): the final tuple
        """

        unity_list = [0 for _ in range(number * number)]
        unity_list[::number + 1] = [1 for _ in unity_list[::number + 1]]
        return __class__(tuple(splitting(unity_list, number)))

    @staticmethod
    def ones(number):
        """Display a tuple of tuples filled with ones.

        Args:
            number(int): the amount of tuples the user wants

        Returns(Matrix): the final tuple
        """

        ones_list = [[1 for _ in range(number)] for _ in range(number)]
        final_mtx = tuple(tuple(x) for x in ones_list)
        return __class__(final_mtx)

    @property
    def tuples(self):
        """Return the instance as tuple.

        Returns(tuple): the raw tuple
        """

        return self.data


def splitting(a_list, slice_number):
    """Split a list into smaller lists and convert them to tuples.

    Args:
        a_list(list): the original unsliced list
        slice_number(int): the amount of small lists post slicing

    Returns: the final list of smaller tuples
    """

    inverted_list = [tuple(a_list[i * len(a_list) // slice_number:
                                  (i + 1) * len(a_list) // slice_number])
                     for i in range(slice_number)]
    return inverted_list
