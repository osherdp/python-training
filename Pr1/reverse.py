def reverse(num_string):
    num_string = num_string[::-1]
    return num_string


def main():
    lst = ['stay', 'cat', 'love', 'aba']
    for i in range(len(lst)):
        lst[i] = reverse(lst[i])
    lst.sort()
    for i in range(len(lst)):
        lst[i] = reverse(lst[i])
    print(lst)


if __name__ == "__main__":
    main()
