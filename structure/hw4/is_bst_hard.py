#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def check(index,tree,low,up):
  node=tree[index]
  if node[0]<low:
    return False
  if node[0]>=up:
    return False
  a=True
  b=True

  if node[1]!=-1:
    upper=min(up,node[0])
    a= check(node[1],tree,low,upper)

  if node[2] != -1:
    lower = max(low, node[0])
    b= check(node[2], tree, lower, up)

  return a and b


def IsBinarySearchTree(tree):
  if len(tree)>0:
    return check(0,tree,-10000000000,10000000000)
  else:
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    a=list(map(int, sys.stdin.readline().strip().split()))
    tree.append(a)
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()