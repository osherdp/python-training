STR_FORMAT = 'Matrix({})'


class Matrix(tuple):

    def __init__(self, tuples=()):
        self.size = len(tuples[0])
        self.rows = tuples
        self.columns = tuple(tuple([t[i]
                                    for t in tuples])
                             for i in range(self.size))
        self.__index = -1

    def __repr__(self):
        return str(self.rows)

    def __str__(self):
        return STR_FORMAT.format(self.rows)

    @property
    def tuples(self):
        return self.rows

    @classmethod
    def unity(cls, size):
        return Matrix(tuple([tuple([1 if i == j else 0
                                    for j in range(size)])
                             for i in range(size)]))

    @classmethod
    def ones(cls, size):
        return Matrix(tuple([tuple([1 for j in range(size)])
                             for i in range(size)]))

    def __add__(self, other):
        return Matrix(tuple([tuple([self.rows[i][j] + other.rows[i][j]
                                    for j in range(self.size)])
                             for i in range(self.size)]))

    def __sub__(self, other):
        return Matrix(tuple([tuple([self.rows[i][j] - other.rows[i][j]
                                    for j in range(self.size)])
                             for i in range(self.size)]))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(tuple([tuple([self.rows[i][j] * other
                                        for j in range(self.size)])
                                 for i in range(self.size)]))
        elif isinstance(other, Matrix):
            return Matrix(tuple([tuple([sum([self.rows[i][k] * other.rows[k][j]
                                             for k in range(self.size)])
                                        for j in range(self.size)])
                                 for i in range(self.size)]))

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(tuple([tuple([self.rows[i][j] * other
                                        for j in range(self.size)])
                                 for i in range(self.size)]))

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(tuple([tuple([self.rows[i][j] / other
                                        for j in range(self.size)])
                                 for i in range(self.size)]))

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        elif self.size != other.size:
            return False
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if other.rows[i][j] != self.rows[i][j]:
                        return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Matrix):
            return True
        elif self.size != other.size:
            return True
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if other.rows[i][j] != self.rows[i][j]:
                        return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index < self.size:
            return self.rows[self.__index]
        else:
            self.__index = -1
            raise StopIteration()

    def __hash__(self):
        return hash(self.rows)
