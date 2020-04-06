class Matrix:
    def __init__(self, tuple_matrix):
        """
        Please insert a matrix as tuple of tuples
        """
        # ========== tuple to list ===============
        my_list = list(tuple_matrix)
        for index in range(len(tuple_matrix)):
            my_list[index] = list(tuple_matrix[index])
        # ========================================
        self.my_list = my_list
        self.my_tuple = tuple_matrix
        self.counter = 0

    def __str__(self):
        return str(self.my_tuple)

    def __repr__(self):
        return 'Matrix({})'.format(self.my_tuple)

    def __next__(self):
        dim = len(self.my_tuple)
        if self.counter < dim:
            res = self.my_tuple[self.counter]
            self.counter += 1
            return res
        self.counter = 0
        raise StopIteration()

    def __iter__(self):
        return self

    def __mul__(self, other):
        new_list = []
        dim = len(self.my_list)
        for i in range(dim):
            new_list.append([0] * dim)
        if issubclass(type(other), Matrix):  # mul by a matrix
            for i in range(dim):  # i - num of column
                new_sub_list = []
                for j in range(dim):  # j - num of row
                    sub_list_1 = self.my_list[i]
                    sub_list_2 = [element[j] for element in other.my_list]
                    res = sum([sub_list_1[k] * sub_list_2[k]
                               for k in range(dim)])
                    new_sub_list.append(res)
                new_list[i] = [element for element in new_sub_list]
        elif issubclass(type(other), int):  # mul by a number
            for i in range(dim):
                sub_list1 = self.my_list[i]
                new_sub_list = [(element * other) for element in sub_list1]
                new_list[i] = new_sub_list
        # ========== list to tuple ===============
        for index in range(dim):
            new_list[index] = (*new_list[index],)
        list2tuple = (*new_list,)
        return Matrix(list2tuple)

    __rmul__ = __mul__

    def __sub__(self, other):
        new_list = []
        dim = len(self.my_list)
        for i in range(dim):
            new_list.append([0] * dim)
        for i in range(dim):
            sub_list_1 = self.my_list[i]
            sub_list_2 = other.my_list[i]
            new_sub_list = [sub_list_1[index] - sub_list_2[index]
                            for index in range(dim)]
            new_list[i] = new_sub_list
        # ========== list to tuple ===============
        for index in range(dim):
            new_list[index] = (*new_list[index],)
        list2tuple = (*new_list,)
        return Matrix(list2tuple)

    def __add__(self, other):
        new_list = []
        dim = len(self.my_list)
        for i in range(dim):
            new_list.append([0] * dim)
        for i in range(dim):
            sub_list_1 = self.my_list[i]
            sub_list_2 = other.my_list[i]
            new_sub_list = [sub_list_1[index] + sub_list_2[index]
                            for index in range(dim)]
            new_list[i] = new_sub_list
        # ========== list to tuple ===============
        for index in range(dim):
            new_list[index] = (*new_list[index],)
        list2tuple = (*new_list,)
        return Matrix(list2tuple)

    def __truediv__(self, other):
        new_list = []
        dim = len(self.my_list)
        for i in range(dim):
            new_list.append([0] * dim)
        for i in range(dim):
            sub_list_1 = self.my_list[i]
            new_sub_list = [sub_list_1[index] / other
                            for index in range(dim)]
            new_list[i] = new_sub_list
        # ========== list to tuple ===============
        for index in range(dim):
            new_list[index] = (*new_list[index],)
        list2tuple = (*new_list,)
        return Matrix(list2tuple)

    def __eq__(self, other):
        return self.my_list == other.my_list

    def __hash__(self):
        return hash(self.my_tuple)

    def get_tuple(self):
        return self.my_tuple

    @classmethod
    def unity(cls, dim):
        unity_matrix = []
        if dim == 1:
            unity_matrix = (1,)
            return 'Matrix({})'.format(unity_matrix)
        sub_list = [0] * dim
        for i in range(dim):
            unity_matrix.append([0] * dim)

        for i in range(dim):
            for j in range(dim):
                if j == i:
                    sub_list[j] = 1
                else:
                    sub_list[j] = 0
            unity_matrix[i] = tuple([element for element in sub_list])
        unity_matrix = tuple(unity_matrix)
        return Matrix(unity_matrix)

    @classmethod
    def ones(cls, dim):
        ones_matrix = []
        if dim == 1:
            ones_matrix = (1,)
            return 'Matrix({})'.format(ones_matrix)
        sub_list = [0] * dim
        for i in range(dim):
            ones_matrix.append([0] * dim)

        for i in range(dim):
            for j in range(dim):
                sub_list[j] = 1
            ones_matrix[i] = tuple([element for element in sub_list])
        ones_matrix = tuple(ones_matrix)
        return Matrix(ones_matrix)

    tuples = property(get_tuple)
