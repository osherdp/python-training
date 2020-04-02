from pip._vendor.msgpack.fallback import xrange


def is_valid(matrix):
    if is_tuple(matrix):
        if is_squared(matrix):
            return True
        else:
            return False
    else:
        return False


def is_squared(matrix):
    squared = True
    rows = matrix.__len__()
    for inside_tuple in matrix:
        column = inside_tuple.__len__()
        if rows != column:
            squared = False
    return squared


def is_tuple(matrix):
    is_tup = True
    if type(matrix) == tuple:
        for inside_tuple in matrix:
            if type(inside_tuple) != tuple:
                is_tup = False
    else:
        is_tup = False
    return is_tup


class Matrix:
    def __init__(self, matrix=((1, 1), (1, 1))):
        if not is_valid(matrix):
            raise ValueError("invalid matrix")
        else:
            self.__matrix = tuple(matrix)

    def unity(self, size=2):
        unity_matrix = []
        for row in xrange(size):
            member = []
            for column in xrange(size):
                if column == row:
                    member.append(1)
                else:
                    member.append(0)
            unity_matrix.append(tuple(member))
        self.__init__(tuple(unity_matrix))

    def ones(self, size=2):
        ones_matrix = []
        for row in xrange(size):
            member = []
            for column in xrange(size):
                member.append(1)
            ones_matrix.append(tuple(member))
        self.__init__(tuple(ones_matrix))

    def tuples(self):
        return self.__matrix

    def scalar_multiplication(self, scalar):
        result = [tuple([x*scalar for x in i]) for i in self.__matrix]
        return tuple(result)

    def addition(self, other_matrix):
        if self.size_comparision(other_matrix):
            result = []
            for i in xrange(self.get_size()):
                matrix1 = self.__matrix[i]
                matrix2 = other_matrix.tuples()[i]
                container = tuple([matrix1[j] + matrix2[j] for j in xrange(self.get_size())])
                result.append(container)
            return tuple(result)
        else:
            print("matrices size is different")

    def subtraction(self, other_matrix):
        if self.size_comparision(other_matrix):
            result = []
            for i in xrange(self.get_size()):
                matrix1 = [x for x in self.__matrix[i]]
                matrix2 = [y for y in other_matrix.tuples()[i]]
                container = tuple(map(lambda x, y: x - y, matrix1, matrix2))
                result.append(container)
            return tuple(result)
        else:
            print("matrices size is different")

    def multiplication(self, other_matrix):
        if self.size_comparision(other_matrix):
            multiplication_result = []
            size = self.get_size()
            matrix1 = self.tuples()
            matrix2 = other_matrix.tuples()
            for i in xrange(size):
                result = []
                row = matrix2[i]
                for j in xrange(size):
                    matrix = matrix1[j]
                    container = tuple(map(lambda x, y: x * y, matrix, row))
                    result.append(sum(container))
                multiplication_result.append(tuple(result))
            return tuple(multiplication_result)
        else:
            print("matrices size is different")

    def size_comparision(self, matrix):
        if self.get_size() == matrix.get_size():
            return True
        else:
            return False

    def get_size(self):
        return self.__matrix.__len__()

    def compare(self, other_matrix):
        if type(other_matrix) == Matrix:
            return self.tuples().__eq__(other_matrix.tuples())
        else:
            return False

    def repr(self):
        matrix = self.tuples()
        for i in matrix:
            line = str(i)
            line = line.replace('(', '| ')
            line = line.replace(')', ' |')
            line = line.replace(',', '')
            print(line)

    def __iter__(self):
        return iter(self.__matrix)

    def __hash__(self):
        return hash(self.__matrix)

    def __str__(self):
        return "{}".format(self.tuples())
