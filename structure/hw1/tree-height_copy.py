# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                # self.n=int(input())
                # self.parent=list(map(int, input().split()))


        def compute_height(self,i):
            if len(i.child)==0:
                return 0

            else:
                return 1+max([self.compute_height(j) for j in i.child])



def main():
  tree = TreeHeight()
  tree.read()
  tree.node_process()
  print(tree.compute_height(tree.root)+1)

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**27)
threading.Thread(target=main).start()
