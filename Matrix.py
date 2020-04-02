class Matrix:
    # in this program Matrix is a tuple of tuples and the inside tuples must be as long as the major ine is.
    # data is the Matrix (tuple) received from the user
    def __init__(self, data):
        counter = 0
        if type(data) is tuple:
            for tup in data:
                if len(tup) == len(data) and type(tup) is tuple:
                    counter += 1
        if counter == len(data):
            self.data = data
        else:
            raise ValueError("Invalid matrix")

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        return f"Matrix: {self.data}"

    # str returns the Matrix in the mathemathic format
    def __str__(self):
        matrix_in_lines = ""
        for i in range(len(self.data)):
            matrix_in_lines += (str(self.data[i]) + "\n")
        return matrix_in_lines

    def get_tuple(self):
        return self.data

    # unity method creates a matrix of zeros with a diagonal of ones (unity is the Matrix's size)
    @staticmethod
    def unity(unit):
        major_list = [[1 if i == index else 0 for i in range(unit)] for index in range(unit)]
        sub_list = [tuple(lt) for lt in major_list]  # convert list of lists to type Matrix. lt are the inside lists
        matrix_to_return = Matrix((tuple(sub_list)))
        return matrix_to_return

    # ones method returns a Matrix full of ones which sizes determined by "unit"
    @staticmethod
    def ones(unit):
        major_list = [([1] * unit) for i in range(unit)]
        sub_list = [tuple(lt) for lt in major_list]  # convert list of lists to type Matrix. lt are the inside lists
        matrix_to_return = Matrix((tuple(sub_list)))
        return matrix_to_return

    def __add__(self, other):
        if type(other) is Matrix:
            ans = []
            for tup in range(len(self.data)):
                ans.append([])
                for num in range(len(self.data)):
                    ans[tup].append(self.data[tup][num] + other[tup][num])
            sub_list = [tuple(ls) for ls in ans]  # convert ans to type Matrix. ls are the inside lists
            matrix_to_return = Matrix((tuple(sub_list)))
            return matrix_to_return
        else:
            raise SyntaxError("only matrix's summery")

    def __sub__(self, other):
        if type(other) is Matrix:
            ans = []
            for tup in range(len(self.data)):
                ans.append([])
                for num in range(len(self.data)):
                    ans[tup].append(self.data[tup][num] - other[tup][num])
            sub_list = [tuple(ls) for ls in ans]  # convert list of lists to type Matrix. ls are the inside lists
            matrix_to_return = Matrix((tuple(sub_list)))
            return matrix_to_return
        else:
            raise SyntaxError("only matrix's subscription")

    def __truediv__(self, other):
        if type(other) is float or int:  # the program doesnt support division by other Matrix
            return self.scalar_mul(1/other)
        else:
            raise SyntaxError("only  scalar division")

    def __mul__(self, other):
        if type(other) is Matrix:  # Matrix's multiplication --->
            ans = []  # will contain the answer as a list of lists.
            new_other = []
            # this loop convert "other" from Matrix type to a list of lists named "new_other".
            for line in range(len(self.data)):
                new_other.append([])
                ans.append([0] * len(self.data))  # ns starts as a list of lists full of zeros.
                for num in range(len(self.data)):
                    new_other[line].append(other[num][line])
            # this is the multiplication process->
            for tup in range(len(self.data)):
                for num in range(len(self.data)):
                    for i in range(len(self.data)):
                        ans[tup][num] += self.data[tup][i] * new_other[num][i]
            # here i added to the zero the summery of the multiplications of any two numbers which
            # their places in the matrices are fits by the matrices multiplication rules.
            sub_list = [tuple(ls) for ls in ans]  # convert ans to type Matrix. ls are the inside lists.
            matrix_to_return = Matrix((tuple(sub_list)))
            return matrix_to_return
        else:
            return self.scalar_mul(other)

    def scalar_mul(self, other):
        ans = []
        for tup in range(len(self.data)):
            ans.append([])
            for num in range(len(self.data)):
                ans[tup].append(self.data[tup][num] * other)
        sub_list = [tuple(ls) for ls in ans]  # convert ans to type Matrix. ls are the inside lists
        matrix_to_return = Matrix((tuple(sub_list)))
        return matrix_to_return

    def __eq__(self, other):
        return self.data == other

    # let matrix instances to be a key in a dictionary.
    def __hash__(self):
        return hash(self.data)
