class Matrix:
    def __init__(self, x):
        if type(x) is tuple:
            for tup in x:
                if len(tup) == len(x) and type(tup) is tuple:
                    self.x = x
                else:
                    self.x = None
                    print("invalid Matrix")
        else:
            self.x = None
            print("invalid matrix")

    def __iter__(self):
        return iter(self.x)

    def __getitem__(self, item):
        return self.x[item]

    def __repr__(self):
        string = ""
        for i in range(len(self.x)):
            string += (str(self.x[i]) + "\n")
        return string

    def __str__(self):
        return "Matrix:" + str(self.x)

    def get_tuple(self):
        return self.x

    @staticmethod
    def unity(unit):
        ls = []
        for i in range(unit):
            ls.append([0] * unit)
            ls[i][i] = 1
        unitup = [tuple(lt) for lt in ls]
        matrix_to_return = Matrix((tuple(unitup)))
        return matrix_to_return

    @staticmethod
    def ones(unit):
        ls = []
        for i in range(unit):
            ls.append([1] * unit)
        unitup = [tuple(lt) for lt in ls]
        matrix_to_return = Matrix((tuple(unitup)))
        return matrix_to_return

    def __add__(self, other):
        if type(other) is Matrix:
            ans = []
            for tup in range(len(self.x)):
                ans.append([])
                for num in range(len(self.x)):
                    ans[tup].append(self.x[tup][num] + other[tup][num])
            unitup = [tuple(ls) for ls in ans]
            matrix_to_return = Matrix((tuple(unitup)))
            return matrix_to_return
        else:
            print("only matrix's summery")

    def __sub__(self, other):
        if type(other) is Matrix:
            ans = []
            for tup in range(len(self.x)):
                ans.append([])
                for num in range(len(self.x)):
                    ans[tup].append(self.x[tup][num] - other[tup][num])
            unitup = [tuple(ls) for ls in ans]
            matrix_to_return = Matrix((tuple(unitup)))
            return matrix_to_return
        else:
            print("only matrix's subscription")

    def __truediv__(self, other):
        if type(other) is float or int:
            ans = []
            for tup in range(len(self.x)):
                ans.append([])
                for num in range(len(self.x)):
                    ans[tup].append(self.x[tup][num]/ other )
            unitup = [tuple(ls) for ls in ans]
            matrix_to_return = Matrix((tuple(unitup)))
            return matrix_to_return
        else:
            print("only  scalar division")

    def __mul__(self, other):
        if type(other) is Matrix:
            ans = []
            new_other = []
            for line in range(len(self.x)):
                new_other.append([])
                ans.append([0]*len(self.x))
                for num in range(len(self.x)):
                    new_other[line].append(other[num][line])
            for tup in range(len(self.x)):
                for num in range(len(self.x)):
                    for i in range(len(self.x)):
                        ans[tup][num] += self.x[tup][i] * new_other[num][i]
            unitup = [tuple(ls) for ls in ans]
            matrix_to_return = Matrix((tuple(unitup)))
            return matrix_to_return
        else:
            ans = []
            for tup in range(len(self.x)):
                ans.append([])
                for num in range(len(self.x)):
                    ans[tup].append(self.x[tup][num] * other)
            unitup = [tuple(ls) for ls in ans]
            matrix_to_return = Matrix((tuple(unitup)))
            return matrix_to_return

    def __eq__(self, other):
        if self.x == other:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.x)