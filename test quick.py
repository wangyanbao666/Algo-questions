# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
    print(k)
    print(a)

if __name__ == '__main__':
    # # input = sys.stdin.read()
    # n, *a = list(map(int, input().split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    # a=range(10,0,-1)
    # for i in a:
    #     print(i)
    # print(i for i in range(10))
    # li=[(1,2),(3,4),(5,6),(2,5)]
    # li[0],li[1]=li[1],li[0]
    # print(li)
    # t=(10,20)<(20,1)
    # print(t)
    # a=[1,2,3,4,5,6,7]
    # a.insert(0,1)
    # a.pop(3)
    # print(a)
    # print(sum(a))
    #
    # for i in range(1,1):
    #     print(i)
    # import copy
    # a=[1,2,3,4,5]
    # b=copy.deepcopy(a)
    # b[1]=0
    # print(a)
    # for i in range(9):
    #     j=i
    #     j+=1
    #     print(j,i)
    # a=2
    # b=a
    # a+=1
    # print(b)

    # import turtle
    #
    # t = turtle.Turtle()  # instantiate one object
    # u = turtle.Turtle()  # instantiate another object
    #
    # # notice how the two objects behave differently and separately from each other.
    # t.shape('turtle')
    # t.penup()
    # t.forward(100)
    #
    # u.shape('triangle')
    # u.penup()
    # u.left(90)
    # u.forward(100)
    #
    # turtle.done()

    # print(int('abcd'))
    # a=[1,2,3,4]
    # a.remove(0)
    # print(-7%5==3%5)
    #
    #
    # dict={1:0,2:0}
    # print(type(dict.values()))

    a=[[1,2],[2,3]]
    b=[]
    b.append(a[1])
    b[0][1]=2
    print(a)


