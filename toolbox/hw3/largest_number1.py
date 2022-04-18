#Uses python3

import sys

def isGreaterOrEqual(digit,maxDigit):
    if int(digit+maxDigit)>=int(maxDigit+digit):
        return True
    else:
        return False




def largest_number(a):
    #write your code here
    res = ""
    while len(a)!=0:
        maxDigit = str(0)
        for x in a:
            if isGreaterOrEqual(x,maxDigit):
                maxDigit = x
        res+=maxDigit
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
