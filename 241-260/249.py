"""
    Prime Subset Sums
    https://www.hackerrank.com/contests/projecteuler/challenges/euler249/problem
    https://projecteuler.net/problem=249
"""


def prime_number(number):
    listOfPrimeNumber = []
    for x in range(number):

        listOfPrimeNumber.append(x)

    return listOfPrimeNumber


if __name__ == "__main__":
    input_int = int(input())
    list_return = prime_number(input_int)
    print(list_return)
