# Uses python3
import numpy as np


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    #write your code here
    digit_str=dataset[::2]
    digit=[]
    for i in range(len(digit_str)):
        digit.append(int(digit_str[i]))
    # print(digit)
    opertator=dataset[1::2]
    # print(opertator)
    Mmatric=np.zeros((len(digit),len(digit)))
    mmatric=np.zeros((len(digit),len(digit)))
    for i in range(len(digit)):
        Mmatric[i,i]=digit[i]
        mmatric[i,i]=digit[i]

    #对角线斜着算
    for j in range(1,len(digit)):
        for i in range(0,len(digit)-j):
            s=i+j
            minv=1000000000000
            maxv=-10000000000005-8+7*4-8+9
            for k in range(i,s):
                # print(opertator[k])
                ex1=evalt(Mmatric[i,k],Mmatric[k+1,s],opertator[k])
                ex2=evalt(Mmatric[i,k],mmatric[k+1,s],opertator[k])
                ex3=evalt(mmatric[i,k],Mmatric[k+1,s],opertator[k])
                ex4=evalt(mmatric[i,k],mmatric[k+1,s],opertator[k])
                minv=min(minv,ex1,ex2,ex3,ex4)
                maxv=max(maxv,ex1,ex2,ex3,ex4)
                # print(minv,maxv)
            Mmatric[i,s]=maxv
            mmatric[i,s]=minv

    # print(mmatric)
    # print(Mmatric)
    return int(Mmatric[0,len(digit)-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
# 5-8+7*4-8+9
