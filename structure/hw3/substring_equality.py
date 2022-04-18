# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.H1=[0]*(len(s)+1)
		self.H2=[0]*(len(s)+1)
		self.m1=1000000007
		self.m2=1000000009
		self.x=35
		self.power1=[1]*(len(s)+1)
		self.power2=[1]*(len(s)+1)

	def precompute(self):
		for i in range(len(s)):
			self.H1[i+1]=((self.x*self.H1[i])%self.m1+ord(self.s[i]))%self.m1
			self.H2[i+1]=((self.x*self.H2[i])%self.m2+ord(self.s[i]))%self.m2

	def computePower(self):
		for i in range(len(s)):
			self.power1[i+1]=(self.power1[i]*self.x)%self.m1
			self.power2[i+1]=(self.power2[i]*self.x)%self.m2

	def ask(self, a, b, l):
		power1=self.power1[l]
		power2=self.power2[l]
		return ((self.H1[a+l]-power1*self.H1[a])%self.m1==(self.H1[b+l]-power1*self.H1[b])%self.m1)\
			   &((self.H2[a+l]-power2*self.H2[a])%self.m2==(self.H2[b+l]-power2*self.H2[b])%self.m2)

s = sys.stdin.readline()
q = int(sys.stdin.readline())
# s=input()
# q=int(input())
solver = Solver(s)
solver.precompute()
solver.computePower()
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
