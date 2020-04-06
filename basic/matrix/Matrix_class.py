class Matrix:
    def __init__(self, tuple_mat):
        self.__mat = tuple_mat

    def __str__(self):
        return str(self.__mat)

    def tuples(self):
        """Displays matrix as a tuple"""
        print(str(self.__mat))
        return self.__mat

    def unity(self, n):
        """Creates a unity matrix
        n - dimensions number"""
        result = (tuple([1 if i == j else 0 for j in range(n)]) for i in range(n))
        self.__mat = tuple(result)
        return self.__mat

    def ones(self, n):
        """Creates a matrix of ones
        n - dimensions number"""
        result = (tuple([1 for j in range(n)]) for i in range(n))
        self.__mat = tuple(result)
        return self.__mat

    def multiplication_sum(self, mat2, i, j, n):
        """Computes single element of result of matrices multiplication"""
        return sum([self.__mat[i][k] * mat2[k][j] for k in range(n)])

    def __add__(self, mat2):
        n = len(self.__mat)
        return tuple(tuple([self.__mat[j][i] + mat2[j][i] for i in range(n)]) for j in range(n))

    def __sub__(self, mat2):
        n = len(self.__mat)
        return tuple(tuple([self.__mat[j][i] - mat2[j][i] for i in range(n)]) for j in range(n))

    def __mul__(self, factor):
        n = len(self.__mat)
        if type(factor) is int or type(factor) is float:
            return tuple(tuple([self.__mat[j][i] * factor for i in range(n)]) for j in range(n))
        else:
            return tuple(tuple(self.multiplication_sum(factor, i, j, n) for j in range(n)) for i in range(n))

    def __truediv__(self, factor):
        n = len(self.__mat)
        return tuple(tuple([self.__mat[j][i] / factor for i in range(n)]) for j in range(n))

    def __ne__(self, mat2):
        n = len(self.__mat)
        for i in range(n):
            for j in range(n):
                if self.__mat[j][i] != mat2[j][i]:
                    return 'True'
        return 'False'
