# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyHash(s,p,x):
    Hp=0
    for i in range(len(s)-1,-1,-1):
        Hp = x * Hp + ord(s[i])
    return Hp%p

def AreEqual(pattern,s):
    for i in range(len(pattern)-1):
        if pattern[i]!=s[i]:
            return False
    return True

def get_occurrences(pattern, text):
    result=[]
    x=1
    p=100000007
    lp=len(pattern)
    lt=len(text)
    power=x**lp
    H=[0]*(lt-lp+1)
    Hp=polyHash(pattern,p,x)
    H[lt-lp]=polyHash(text[lt-lp:],p,x)
    for l in range(lt-lp-1,-1,-1):
        H[l]=(x*H[l+1]+ord(text[l])-ord(text[l+lp])*power)%p

    for i in range(len(H)):
        if H[i]==Hp:
            # print(text[i:i+len(pattern)])
            if pattern==text[i:i+lp]:
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

