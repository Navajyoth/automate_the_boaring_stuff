def collatz(number):
    if number % 2 == 0:
        output = number // 2
        print(output)
        return output
    else:
        output = 3 * number + 1
        print(output)
        return output


def collatzSequence():
    print('Enter your number.')
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        print('You must enter an integer')

collatzSequence()
