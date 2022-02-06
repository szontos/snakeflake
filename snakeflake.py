import time    # purpose: to measure the time required to solve the problem
import os



def problem_1(number):
    my_sum = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            my_sum += i
    return my_sum


def problem_2(option='even'):
    summary = 0
    start = time.time()
    for n in range(100):
        if fibonacci_of(n) <= 4_000_000:
            if fibonacci_of(n) % 2 == 0:
                summary += fibonacci_of(n)
                print(f'{fibonacci_of(n):>12_}')
    end = time.time()
    print(f'Duration: {end-start}\n')
    print(f'Summary: {summary:,}')


def fibonacci_of(n):
    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


def problem_3(number):
    factors = []
    primes = []
    prime_flag = False
    for i in range(2, number):
        if number%i == 0:
            factors.append(i)
    for factor in factors:
        for i in range(2, factor):
            if factor%i == 0:
                prime_flag = True
                primes.append(i)
        prime_flag = False

    print(factors)
    print(primes)

    return max(primes)


def problem_10(n=10):
    '''Problem 10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    Sieve of Eratosthenes.'''
    m = n+1
    #numbers = [True for i in range(m)]
    numbers = [True] * m #EDIT: faster
    for i in range(2, int(n**0.5 + 1)):
        if numbers[i]:
          for j in range(i*i, m, i):
            numbers[j] = False
        primes = []

    for i in range(2, m):
        if numbers[i]:
            primes.append(i)

    print(primes)
    print(sum(primes))


def problem_13(file_path):
    '''Problem 13
    Work out the first ten digits of the sum
    of the following one-hundred 50-digit numbers.
    There is a separate text file which contains
    the one-hundred numbers'''
    exists = os.path.exists(file_path)
    if exists:
        f = open(file_path, 'r')
        numbers = f.readlines()
        f.close()
        summary = 0
        for number in numbers:
            #summary += int(number[:11])  #this also works
            summary += int(number)
        str_summary = str(summary)
        print(str_summary[0:10])


if __name__ == '__main__':
    start = time.time()

    # problem 13
    file_path = r'D:\PYTHON\project_Euler\problem_13.txt'
    problem_13(file_path)

    end = time.time()
    print(f'Time:', end - start)
