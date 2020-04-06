from Matrix import Matrix


def main():
    a = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    b = Matrix(((6, 1, 5), (3, 1, 4), (-7, 4, 1)))
    c = Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    # print(type(a))
    # print(repr(a != b))
    # print(repr(a.tuples))
    # print(repr(Matrix.ones(5)))
    # print(b)
    print(a * b)
    # print(a.my_list)
    # print(a.tuples)
    # print(a + b)
    # print(a * b)
    # print(Matrix.unity(3).my_tuple)
    print(repr(c - Matrix.ones(3)))
    # print(c == (Matrix.unity(3)))
    for line in a:
        print(line)

    dictionary = {Matrix(((1, 1), (2, 2))): 2, Matrix(((1, 1), (2, 3))): 3}
    print(dictionary)


if __name__ == '__main__':
    main()
