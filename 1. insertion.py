a=[1,23,21,45,46,23,7,9]

for i in range(1,len(a)):
    key=a[i]
    while i>0 and a[i-1]<key:#key不是a[i]
        a[i]=a[i-1]
        i-=1
    a[i]=key

print(a)










