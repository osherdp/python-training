import sys

FILE1 = 1
FILE2 = 2


def main():
    try:
        with open(sys.argv[FILE1], 'r') as f1:
            with open(sys.argv[FILE2], 'w') as f2:
                f_content = f1.read().split('\n')
                print(f_content)

                new_content = (list(map(lambda x: 'liel' + ' ' + x + ' ' + 'yaakobov', f_content)))
                print(new_content)

                for i in new_content:
                    # print(i)
                    f2.writelines("{}\n".format(i))

        with open(sys.argv[FILE2], 'r') as f:
            print(f.read())

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
