try:
    num1 = int(input('Gimme the first number\n'))
    num2 = int(input('Gimme the second number\n'))
except ValueError:
    print('you have entered letters instead numbers')
else:
    print(f'the sum of the wo numbers is {num1 + num2}')

