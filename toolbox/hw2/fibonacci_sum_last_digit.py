# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    pm = 1
    cm = 1
    Fi = [1]

    # 找到循环节
    while not (pm == 0 and cm == 1):
        previous, current = current, previous + current
        Fi.append(current)
        pm = previous % 10
        cm = current % 10
    count = len(Fi) - 1


    num = (n+2) % count
    result = (Fi[num - 1]-1) % 10

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
