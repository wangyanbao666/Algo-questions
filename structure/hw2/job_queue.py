# python3

from collections import namedtuple
from copy import deepcopy

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def build_heap(data):
    length=len(data)
    for i in range(length//2-1,-1,-1):
        j=i
        while True:
            maxindex=j
            l=2*j+1
            if l<length:
                if data[l]<data[maxindex]:
                    maxindex=l
            r=2*j+2
            if r<length:
                if data[r]<data[maxindex]:
                    maxindex=r
            if j==maxindex:
                break
            else:
                data[j],data[maxindex]=data[maxindex],data[j]
                j=maxindex
    return data


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    heap = [[i,0] for i in range(n_workers)]
    work_list=[]
    index=len(jobs)
    for job in jobs:
        i=0
        a = heap[0][0]
        b = heap[0][1]
        work_list.append((a, b))
        heap[0][1] += job
        while 2*i+1<n_workers:
            test = i
            l=2*i+1
            r=2*i+2
            if r<n_workers:
                if heap[l][1]==heap[r][1]:
                    if heap[l][0]>heap[r][0]:
                        swap=r
                    else:
                        swap=l
                elif heap[l][1]>heap[r][1]:
                    swap=r
                elif heap[l][1]<heap[r][1]:
                    swap=l
                if heap[i][1]>heap[swap][1]:
                    heap[i],heap[swap]=heap[swap],heap[i]
                    i = swap
                elif heap[i][1]==heap[swap][1]:
                    if heap[i][0]>heap[swap][0]:
                        heap[i],heap[swap]=heap[swap],heap[i]
                        i=swap
            else:
                if heap[i][1]>heap[l][1]:
                    heap[i],heap[l]=heap[l],heap[i]
                    i=l
                elif heap[i][1]==heap[l][1]:
                    if heap[i][0]>heap[l][0]:
                        heap[i],heap[l]=heap[l],heap[i]
                        i=l
            if test==i:
                break
        # print(heap)


        # print(work_list)
        # print(heap)
    return work_list


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
