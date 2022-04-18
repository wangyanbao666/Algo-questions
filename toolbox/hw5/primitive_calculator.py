# Uses python3
import sys

def optimal_sequence(n):
    operation=[0,0]
    sequence = [n]
    li=[0]*(n+1)
    for i in range(2,n+1):
        minnum=10000000000000
        if i%3==0:
            t1=li[int(i/3)]+1
            if t1<minnum:
                minnum=t1
        else:
            t1=100000000000

        if i%2==0:
            t2=li[int(i/2)]+1
            if t2<minnum:
                minnum=t2
        else:
            t2=100000000000
        t3=li[i-1]+1
        if t3<minnum:
            minnum=t3
        li[i]=minnum
        if minnum==t1:
            operation.append(1)
        elif minnum==t2:
            operation.append(2)
        else:
            operation.append(3)
    re=n
    while re>1:
        if operation[int(re)] == 1:
            re /= 3
        elif operation[int(re)] == 2:
            re /= 2
        else:
            re -= 1
        sequence.append(int(re))
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

