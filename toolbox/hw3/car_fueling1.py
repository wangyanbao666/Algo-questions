# python3
import sys


def compute_min_refills(distance, tank, stops):
    i=0
    num=0
    stops.insert(0,0)
    stops.append(distance)
    while i<len(stops)-1:
        current=i
        while i<len(stops)-1 and stops[i+1]-stops[current]<=tank:
            i+=1
        if current==i:
           return -1
        num+=1
    return num-1

if __name__ == '__main__':
    # d, m, _, *stops = map(int, input().split())
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
# 950 400 4 200 375 550 750
