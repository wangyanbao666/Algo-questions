# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    pm = 1
    cm = 1
    Fi=[1]

    #找到循环节
    while not (pm == 0 and cm == 1):
        previous, current = current, previous + current
        Fi.append(current)
        pm =previous%m
        cm=current%m
    count=len(Fi)-1


    num=n%count
    result=Fi[num-1]%m if num!=0 else 0

    return result

if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
