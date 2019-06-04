def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


def my_factorial(num):
    """Calculate the factorial"""

    print('test my factorial')

    def factorial(num):
        print(f'factorial factor: {num}')
        if num == 1:
            return 1

        return num * factorial(num - 1)

    return factorial(num)


print(factorial(4))

print(my_factorial(4))

print(factorial(3))
