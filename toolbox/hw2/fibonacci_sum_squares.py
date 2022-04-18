# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    pm = 1
    cm = 1
    Fi=[1]

    # 找到循环节
    while not (pm == 0 and cm == 1):
        previous, current = current, previous + current
        Fi.append(current)
        pm = previous % 10
        cm = current % 10
    count = len(Fi) - 1


    num1=n%count
    result1=Fi[num1]%10
    result2=Fi[num1-1]%10 if num1!=0 else 0
    result=(result1*result2)%10

    return result

if __name__ == '__main__':
    # n = int(stdin.read())
    n=int(input())
    print(fibonacci_sum_squares_naive(n))
