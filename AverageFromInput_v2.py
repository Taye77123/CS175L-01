
def main():

    total = 0.0
    length = 0.0
    average = 0.0

    try:
        
        numbers.txt = input('numbers.txt')

        
        infile = open(numbers.txt, 'r')

        
        contents = infile.read()

        
        print(contents)

        
        for line in infile:
            amount = float(line)
            total += amount
            length = length + 1

        average = total / length

        
        infile.close()

        
        print('There were ', length, ' numbers in the file.' )
        print(format(average, ',.2f'))

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file')
