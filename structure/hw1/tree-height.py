# python3

import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class node():
    def __init__(self,key):
        self.key=key
        self.child=[]
        self.height=1


class TreeHeight:
        def read(self):
                # self.n = int(sys.stdin.readline())
                # self.parent = list(map(int, sys.stdin.readline().split()))
                self.n=int(input())
                self.parent=list(map(int, input().split()))
                self.node_list=[]
                self.root=None

        def node_process(self):
            for i in self.parent:
                n=node(i)
                self.node_list.append(n)
            for i in self.node_list:
                if i.key==-1:
                    self.root=i
                else:
                    p_pos=i.key
                    p_node=self.node_list[p_pos]
                    p_node.child.append(i)
            # for i in self.node_list:
            #     print(i.key)
            #     print('left:',i.left)
            #     print('right:',i.right)

        def compute_height(self):
            queue=[self.root]
            height=0
            while len(queue)!=0:
                newqueue=[]
                for i in queue:
                    newqueue+=i.child
                queue=newqueue
                height+=1
            return height



def main():
  tree = TreeHeight()
  tree.read()
  tree.node_process()
  print(tree.compute_height())


threading.Thread(target=main).start()
