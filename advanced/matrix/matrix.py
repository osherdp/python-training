class Matrix:

    def __init__(self, matrix_values):
        self._tuples = matrix_values
        self.size = len(self.tuples)
        return

    @property
    def tuples(self):
        return self._tuples

    def __hash__(self):
        return hash(self.tuples)

    def __str__(self):
        return "{}".format(self.tuples)

    def __repr__(self):
        return "Matrix({})".format(self.tuples)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.size:
            value = self.tuples[self.counter]
            self.counter += 1
            return value
        else:
            raise StopIteration

    def __add__(self, other):
        size = self.size
        sum_list = []
        sum_raw = []
        for i in range(0, size):
            for j in range(0, size):
                sum_raw.append(int(self.tuples[i][j]) + int(other.tuples[i][j]))
            sum_list.append(tuple(sum_raw))
            sum_raw = []

        sum_mat = Matrix(tuple(sum_list))
        return sum_mat

    def __sub__(self, other):
        size = self.size
        sub_list = []
        sub_raw = []
        for i in range(0, size):
            for j in range(0, size):
                sub_raw.append(int(self.tuples[i][j]) - int(other.tuples[i][j]))
            sub_list.append(tuple(sub_raw))
            sub_raw = []

        sub_mat = Matrix(tuple(sub_list))
        return sub_mat

    def __truediv__(self, scalar):
        size = self.size
        div_list = []
        div_raw = []
        for i in range(0, size):
            for j in range(0, size):
                div_raw.append(int(self.tuples[i][j]) / scalar)
            div_list.append(tuple(div_raw))
            div_raw = []

        div_mat = Matrix(tuple(div_list))
        return div_mat

    def __rmul__(self, other):
        return Matrix.matrix_scalar_mul(self, other)

    def __mul__(self, other):
        if type(other) is int:
            return Matrix.matrix_scalar_mul(self, other)
        else:
            size = self.size
            mul_list = []
            mul_raw = []
            entry = 0
            for i in range(0, size):
                for j in range(0, size):
                    for k in range(0, size):
                        entry += int(self.tuples[i][k]) * int(other.tuples[k][j])
                    mul_raw.append(entry)
                    entry = 0
                mul_list.append(tuple(mul_raw))
                mul_raw = []
            mul_mat = Matrix(tuple(mul_list))
            return mul_mat

    def matrix_scalar_mul(self, scalar):
        size = self.size
        mul_list = []
        mul_raw = []
        for i in range(0, size):
            for j in range(0, size):
                mul_raw.append(int(self.tuples[i][j]) * scalar)
            mul_list.append(tuple(mul_raw))
            mul_raw = []

        mul_mat = Matrix(tuple(mul_list))
        return mul_mat

    def __eq__(self, other):
        if self.size != other.size:
            return False
        size = len(self.tuples)
        for i in range(0, size):
            for j in range(0, size):
                if self.tuples[i][j] != other.tuples[i][j]:
                    return False

        return True

    def __ne__(self, other):
        if self.size != other.size:
            return True
        size = len(self.tuples)
        for i in range(0, size):
            for j in range(0, size):
                if self.tuples[i][j] != other.tuples[i][j]:
                    return True

        return False

    @classmethod
    def ones(cls, size):
        matrix_list = []
        matrix_ones = tuple("1" * size)
        [matrix_list.append(matrix_ones)
         for i in range(0, size)]

        ones_mat = Matrix(tuple(matrix_list))
        return ones_mat

    @classmethod
    def unity(cls, size):
        matrix_list = []
        matrix_zeros = "0" * size
        [matrix_list.append(tuple(matrix_zeros[0:i] + '1' + matrix_zeros[i:-1]))
         for i in range(0, size)]

        unity_mat = Matrix(tuple(matrix_list))
        return unity_mat
