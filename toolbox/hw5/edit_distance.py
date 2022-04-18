# Uses python3
import numpy as np

def edit_distance(s, t):
    matric=np.zeros((len(s)+1,len(t)+1))
    for i in range(len(s)+1):
        matric[i,0]=i
    for j in range(len(t)+1):
        matric[0,j]=j
    # print(matric)
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            de=matric[i-1,j]+1
            ins=matric[i,j-1]+1
            mismatch=matric[i-1,j-1]+1
            match=matric[i-1,j-1]
            if s[i-1]==t[j-1]:
                matric[i,j]=min(de,ins,match)
            else:
                matric[i,j]=min(de,ins,mismatch)
    # print(matric)
    return int(matric[len(s),len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
