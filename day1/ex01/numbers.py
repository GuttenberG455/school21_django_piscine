
def print_numbers():
    f = open("numbers.txt", 'r')
    for line in f.readlines():
        num_list = line.split(',')
        for number in num_list:
            print(number)
    f.close()


if __name__ == '__main__':
    print_numbers()
