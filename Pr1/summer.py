def summer(lst):
    flag = 0
    temp = 0
    for i in range(len(lst)):
        if issubclass(type(lst[i]), list):
            flag = 1
    if (flag == 0) and (issubclass(type(lst[0]), str)):
        new_str = ''
        for i in range(len(lst)):
            new_str = new_str + lst[i]
        print(new_str)
    elif flag == 0:
        new_str = sum(lst)
        print(new_str)
    else:
        new_str = []
        for i in range(len(lst)):
            temp = lst[i]
            if issubclass(type(temp), list):
                new_str = new_str + temp
            else:
                new_str = new_str + temp.split()
        print(new_str)
        print(lst)


def main():
    summer(['aa', 'bb', 'cc'])


if __name__ == "__main__":
    main()
