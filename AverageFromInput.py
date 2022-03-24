
import math

def find_numbers():

    num_list = []

    with open ('numbers.txt', 'r') as f:
        for line in f:
            num = line.strip()
            num_list += [num]
            return (num_list)

    def main():
        find_numbers('numbers.txt')
        print(num_list)

    main()
