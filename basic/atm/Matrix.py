_ather_ = 'shaked manor'
# this script receive squared matrices and can do mathematical actions on it,
# adding, subtracting, multiplying dividing and compering.

class Matrix:
    """ this class defined the matrix as a member,
     and containing the methods that commit the mathematical actions on the matrix  """
    def __init__(self, matrix_item):
        self.matrix_tuple = tuple(matrix_item)
        matrix_list = []
        for i in xrange(len(matrix_item)):
            matrix_list.append(list(matrix_item[i]))
        self.matrix_list = matrix_list

    def __repr__(self):
        return '{}'.format(self.matrix_tuple)

    def __str__(self):
        return str(self.matrix_tuple)

    def __add__(self, add):
        """adding to the matrix either another matrix or a scalar/
        arg: add- the other matrix or scalar were like to add with"""
        add_list = []
        sum_list =[]
        for i in range(len(self.matrix_list)):
            add_list.append(list(add.matrix_list[i]))
        for i in range(len(self.matrix_list)):
            sublist = self.matrix_list[i]
            sublist2 = add_list[i]
            for num in range(len(sublist)):
                sublist[num] += sublist2[num]
            sum_list.append(tuple(sublist))

        return Matrix(tuple(sum_list))



    def __sub__(self, subtract):
        """subtracting from the matrix either another matrix or a scalar,
        arg: subtract- the other matrix or scalar were like to subtract with"""
        subtract_list = []
        sum_list =[]
        for i in range(len(self.matrix_list)):
            subtract_list.append(list(subtract.matrix_list[i]))
        for i in range(len(self.matrix_list)):
            sublist = self.matrix_list[i]
            sublist2 = subtract_list[i]
            for num in range(len(sublist)):
                sublist[num] -= sublist2[num]
            sum_list.append(tuple(sublist))

        return Matrix(tuple(sum_list))


    def __truediv__(self, divide):
        """divides the matrix with another matrix or a scalar,
        arg: divide- the other matrix or scalar were like to divide with"""
        sum_list = []
        for i in range(len(self.matrix_list)):
            sublist = self.matrix_list[i]
            for num in range(len(sublist)):
                sublist[num] /= float(divide)
            sum_list.append(tuple(sublist))

        return Matrix(tuple(sum_list))

    def __mul___(self, another_matrix):
        """multiplies the matrix with another matrix or a scalar,
        arg: another matrix- the other matrix or scalar were like to multiply with"""
        if type(another_matrix)== int or float:
            sum_list = []
            for i in range(len(self.matrix_list)):
                sublist = self.matrix_list[i]
                for num in range(len(sublist)):
                    sublist[num] *= scalar
                sum_list.append(tuple(sublist))

            return Matrix(tuple(sum_list))
        else:
            sum_list = []
            sum_raws = []
            for num_of_raw in range(len(self.matrix_list)):
                raw = self.matrix_list[num_of_raw]
                sum_raw = []
                for place_in_another_matrix_raw in range(len(raw)):
                    sum_num = 0
                    for num_in_raw in range(len(raw)):
                        raw_in_another_matrix = another_matrix.matrix_list[num_in_raw]
                        result = raw[num_in_raw] * raw_in_another_matrix[place_in_another_matrix_raw]
                        sum_num += result
                    sum_raw.append(sum_num)
                sum_raws.append(tuple(sum_raw))
            sum_list.append(tuple(sum_raws))
            return Matrix(sum_list)


    def __eq__(self, another_matrix):
        """compares the matrix with an arg, and returning true or false."""
        if self.matrix_list == another_matrix.matrix_list:
            return True
        elif self.matrix_list != another_matrix.matrix_list:
            return False

    @property
    def tuples(self):
        return self.matrix_tuple


    @classmethod
    def unity(cls, unity_num):
        unity_list = []
        for num_of_raw in range(unity_num):
            raw = []
            for spot_in_raw in range(unity_num):
                if spot_in_raw == num_of_raw:
                    raw.append(1)
                else:
                    raw.append(0)
            unity_list.append(tuple(raw))
        return Matrix(tuple(unity_list))

    @classmethod
    def ones(cls, unity_num):
        unity_list = []
        for num_of_raw in range(unity_num):
            raw = []
            for spot_in_raw in range(unity_num):
                raw.append(1)
            unity_list.append(tuple(raw))
        return Matrix(tuple(unity_list))

    def __hash__(self):
        return hash(self.matrix_tuple)


def main():
    a = Matrix(((1, 2), (3, 4)))
    b = Matrix(((3, 5),(6, 8)))
    dictionary = {a: 1, b: 2}

main()


