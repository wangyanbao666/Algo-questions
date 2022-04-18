# python3
import copy

def max_sliding_window_naive(sequence, m):
    length=len(sequence)
    largest=[]
    maximums=[]
    count_large=0
    for i in range(length):

        if count_large<i-m+1:
            largest.pop(0)
            count_large+=1
        # print(largest)

        for j in largest[:]:
            if j<=sequence[i]:
                largest.remove(j)
                count_large += 1


        largest.append(sequence[i])

        # print(largest)

        # print(count_large,i)

        if i>=m:
            maximums.append(largest[0])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

