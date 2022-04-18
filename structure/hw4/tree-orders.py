# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrderImplement(self,n,ls):
    if self.left[n]!=-1:
        self.inOrderImplement(self.left[n],ls)
    ls.append(self.key[n])
    if self.right[n]!=-1:
        self.inOrderImplement(self.right[n],ls)

  def preOrderImplement(self,n,ls):
    ls.append(self.key[n])
    if self.left[n]!=-1:
        self.preOrderImplement(self.left[n],ls)
    if self.right[n]!=-1:
        self.preOrderImplement(self.right[n],ls)

  def postOrderImplement(self,n,ls):
      if self.left[n] != -1:
          self.postOrderImplement(self.left[n], ls)
      if self.right[n] != -1:
          self.postOrderImplement(self.right[n], ls)
      ls.append(self.key[n])

  def inOrder(self):
    self.result = []
    self.inOrderImplement(0,self.result)
                
    return self.result

  def preOrder(self):
    self.result = []
    self.preOrderImplement(0,self.result)
                
    return self.result

  def postOrder(self):
    self.result = []
    self.postOrderImplement(0,self.result)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
