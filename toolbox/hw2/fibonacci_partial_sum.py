# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
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


    num1 = (n+2) % count
    result1 = (Fi[num1 - 1]-1) % 10
    num2=(m+1)%count
    result2=(Fi[num2 - 1]-1) % 10
    result=result1-result2 if result1>=result2 else result1+10-result2

    return result

if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))