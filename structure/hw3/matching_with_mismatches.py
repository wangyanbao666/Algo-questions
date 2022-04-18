# python3

import sys

class Solver():
	def __init__(self,k, s, pattern):
		self.s = s
		self.p=pattern
		self.pl=len(pattern)
		self.k=k

		self.H1=[0]*(len(s)+1)
		self.H2=[0]*(len(s)+1)
		self.m1=1000000007
		self.m2=1000000009
		self.x=35
		self.power1=[1]*(self.pl+1)
		self.power2=[1]*(self.pl+1)

		self.patternHash1=[0]*(self.pl+1)
		self.patternHash2=[0]*(self.pl+1)

		self.test=0

		self.computePower()
		self.precompute()
		self.computePattern()
		#
		# print(self.H1)
		# print(self.patternHash1)
		# print(self.power1)

	def computePower(self):
		for i in range(self.pl):
			self.power1[i+1]=(self.power1[i]*self.x)%self.m1
			self.power2[i+1]=(self.power2[i]*self.x)%self.m2

	def precompute(self):
		for i in range(len(self.s)):
			self.H1[i+1]=((self.x*self.H1[i])%self.m1+ord(self.s[i]))%self.m1
			self.H2[i+1]=((self.x*self.H2[i])%self.m2+ord(self.s[i]))%self.m2


	def computePattern(self):
		l=len(self.p)
		for i in range(l):
			self.patternHash1[i+1]=((self.patternHash1[i]*self.x)%self.m1+ord(self.p[i]))%self.m1
			self.patternHash2[i+1]=((self.patternHash2[i]*self.x)%self.m2+ord(self.p[i]))%self.m2

	def compare(self,l,r,i):
		# print(l,r)

		if (self.H1[r]-self.power1[r-l]*self.H1[l])%self.m1==(self.patternHash1[r-i]-self.patternHash1[l-i]*self.power1[r-l])%self.m1 and \
			(self.H2[r]-self.power2[r-l]*self.H2[l])%self.m2==(self.patternHash2[r-i]-self.patternHash2[l-i]*self.power2[r-l])%self.m2:
			# print('true')
			return
		else:
			if l >= r-1:
				# print('test1')
				self.test+=1
				return
			else:
				mid = (l + r) // 2
				self.compare(l, mid,i)
				self.compare(mid, r,i)

	def solve(self):
		ans=[]
		for i in range(len(self.s)-self.pl+1):
			self.test=0
			self.compare(i,i+self.pl,i)
			# print('test:',self.test)
			if self.test<=self.k:
				ans.append(i)
		return ans


for line in sys.stdin.readlines():
# for line in range(4):
	k, t, p = line.split()
	solver = Solver(int(k), t, p)
	ans=solver.solve()
	print(len(ans), *ans)
