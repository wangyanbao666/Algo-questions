# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i=0
    while n-i-1>i+1:
        i+=1
        summands.append(i)
        n-=i
    summands.append(n)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
