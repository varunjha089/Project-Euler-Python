"""
    https://projecteuler.net/problem=1
    https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""


"""
    https://projecteuler.net/problem=1
    https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""


def no_div_by_three_and_five(NUMBER):
    number_list = []
    for i in range(3, NUMBER):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append(i)
    return sum(number_list)


if __name__ == "__main__":
    NO_OF_TEST_CASES = int(input())
    for i in range(NO_OF_TEST_CASES):
        NUMBER = int(input())
        SUM_OF_NUMBER = no_div_by_three_and_five(NUMBER)
        print(SUM_OF_NUMBER)
