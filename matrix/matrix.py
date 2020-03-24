import operator
from itertools import repeat


class Matrix:
    """An immutable object representing a matrix data-type. This
    implementation only supports even-side matrices (n * n).

    Attributes:
        _matrix (tuple): contains the data about the matrix. Each line of
                         the matrix is represented by a tuple.
    """
    __slots__ = '_matrix'

    def __init__(self, *lines):
        if not self._is_valid_data(*lines):
            raise ValueError('Data is not valid')

        super(Matrix, self).__setattr__('_matrix', tuple(lines))

    def __setattr__(self, key, value):
        """Defines that Matrix attributes are immutable."""
        raise AttributeError(f'{self.__class__} instance cannot be modified')

    @staticmethod
    def _is_valid_data(*data: tuple) -> bool:
        """Checks if the data given is valid. Valid data is defined if it
        contains tuples of the same length (Matrix only supports n * n) and
        their value is an integer."""
        # check if each line is a tuple.
        if not all([isinstance(line_data, tuple) for line_data in data]):
            return False

        # check if each item in each line is an int.
        if not all([any([isinstance(item, int), isinstance(item, float)]) for
                    line_data in data for item in line_data]):
            return False

        # checks if the given data is of a n * n matrix.
        if not all([len(line) == len(data) for line in data]):
            return False

        return True

    @classmethod
    def unity(cls, number_lines: int):
        """Generates a matrix with a main diagonal of 1's, everything else
        is 0's.
        """
        tuples_in_chars = [
            list(str('1' + ('0' * i)).zfill(number_lines)[::-1]) for i in
            range(number_lines)]

        return cls(*tuple(
            [tuple(map(int, tuple_chars)) for tuple_chars in tuples_in_chars]))

    @classmethod
    def ones(cls, number_lines):
        """Generates a matrix full of 1's."""
        return cls(*tuple(
            [tuple(repeat(1, number_lines)) for _ in range(number_lines)]))

    def __repr__(self):
        """Returns a string presentation of the matrix instance."""
        return f"({', '.join([str(line) for line in self._matrix])})"

    @property
    def tuples(self):
        """Returns the matrix instance as a tuple of tuples."""
        return self._matrix

    @staticmethod
    def _bool_operation(operation, data) -> bool:
        """Checks boolean operation output.

        Args:
            operation (function): the boolean function to operate.
            data (list): the data of the matrix (list of tuples).

        Returns:
            If the operation is 'equal', returns true if all items are equal
            to their parallel items in other, else false. If operation is
            'not equal', return true if one or more items are not equal to
            their parallel item/s in other, else false.
        """
        if operation == operator.eq:
            return all(
                [item for line_data in data for item in line_data])

        elif operation == operator.ne:
            return any(
                [item for line_data in data for item in line_data])

    def _calculate_matrix_on_matrix(self, other, operation):
        """Does mathematical operation on two matrices.

        Args:
            other (Matrix): the second matrix to do the operation on.
            operation (function): the mathematical function to operate.

        Returns:
            List of tuples which contains the calculated matrix data.
        """
        return [tuple([operation(self.tuples[i][j], other.tuples[i][j]) for j
                       in range(len(self.tuples))]) for i in range(len(
                        self.tuples))]

    def _calculate_scalar_on_matrix(self, other, operation):
        """Does mathematical operation on scalar and matrix.

        Args:
            other (int or float): the scalar.
            operation (function): the mathematical function to operate.

        Returns:
            List of tuples which contains the calculated matrix data.
        """
        return [tuple([operation(self.tuples[i][j], other) for j in range(
            len(self.tuples))]) for i in range(len(self.tuples))]

    def _operations_on_matrix(self, other, operation):
        """Does all the operation that can be done on a matrix.
        addition, subtraction, multiplication and division(on matrix or by
        scalar). Also supports boolean operators == and !=.

        Args:
            other (Matrix or int or float): the other object to do the
                                            operation.
            operation (function): the function of the desired operator.

        Returns:
            If boolean operation, returns true if operation returned true
            else false. If mathematical operation, returns a new matrix with
            the calculated data.
        """
        if isinstance(other, Matrix):

            if len(self.tuples) != len(other.tuples) and not any(
                    [operation == operator.eq, operation == operator.ne]):
                raise ValueError("Matrices length don't match")

            matrix_data = self._calculate_matrix_on_matrix(other, operation)

            if operation == operator.eq or operation == operator.ne:
                return self._bool_operation(operation, matrix_data)

            return Matrix(*matrix_data)

        elif any([isinstance(other, int) or isinstance(other, float)]) and any(
                [operation == operator.mul, operation == operator.truediv]):
            return Matrix(*self._calculate_scalar_on_matrix(other, operation))

        else:
            raise ValueError(f"{operation} not supported on {type(other)}")

    def __add__(self, other):
        """Adds two matrices."""
        return self._operations_on_matrix(other, operator.add)

    def __sub__(self, other):
        """Subtract two matrices."""
        return self._operations_on_matrix(other, operator.sub)

    def __mul__(self, other):
        """Multiply two matrices or scalar by matrix."""
        return self._operations_on_matrix(other, operator.mul)

    def __rmul__(self, other):
        """Defines to handle reverse multiplication (10 * matrix) as regular
        multiplication."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divides two matrices or scalar by matrix. Returns floats if
        needed."""
        return self._operations_on_matrix(other, operator.truediv)

    def __floordiv__(self, other):
        """Defines to handle floor division (5 / 2 = 2) as regular
        division."""
        return self.__truediv__(other)

    def __eq__(self, other):
        """Compares two matrices. Returns true if they are equal else false."""
        return self._operations_on_matrix(other, operator.eq)

    def __ne__(self, other):
        """Compares two matrices. Returns true if they are not equal else
        false."""
        return self._operations_on_matrix(other, operator.ne)

    def __iter__(self):
        """Enables to iterate on a matrix lines'."""
        return iter(self.tuples)

    def __hash__(self):
        """Enables to use a matrix as key of a dictionary."""
        return hash(self.tuples)
