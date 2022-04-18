# Uses python3
def calc_fib(n):
    previous=0
    current=1
    if n<=1:
        return n
    for i in range(n-1):
        previous,current=current,current+previous
    return current

n = int(input())
print(calc_fib(n))

