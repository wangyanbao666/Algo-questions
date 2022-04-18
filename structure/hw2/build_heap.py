# python3


def build_heap(data):
    swaps = []
    length=len(data)
    for i in range(length//2-1,-1,-1):
        j=i
        while True:
            maxindex=j
            l=2*j+1
            if l<length:
                if data[l]<data[maxindex]:
                    # data[l],data[maxindex]=data[maxindex],data[l]
                    maxindex=l
            r=2*j+2
            if r<length:
                if data[r]<data[maxindex]:
                    # data[r],data[maxindex]=data[maxindex],data[r]
                    maxindex=r
            if j==maxindex:
                break
            else:
                swaps.append((j,maxindex))
                data[j],data[maxindex]=data[maxindex],data[j]
                j=maxindex
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
