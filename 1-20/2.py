"""
    https://projecteuler.net/problem=2
    https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

    worked on both
"""


def feb_no(number):
    feb_no_list = [1, 2]

    for i in range(2, number):
        if feb_no_list[-1] > number:
            break
        else:
            result = feb_no_list[i - 2] + feb_no_list[i - 1]
            feb_no_list.append(result)

    feb_no_list.pop(-1)

    sum_of_even_feb = 0
    for x in feb_no_list:
        if x % 2 == 0:
            sum_of_even_feb += x
    return sum_of_even_feb


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        feb_no_result = feb_no(n)
        print(feb_no_result)
