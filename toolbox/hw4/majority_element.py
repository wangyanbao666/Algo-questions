# Uses python3
import sys

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    # #write your code here
    # return -1
    dic={}
    for i in a:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]+=1
    if max(dic.values())>len(a)/2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    print(get_majority_element(a,0,n))


#5 2 3 9 2 2