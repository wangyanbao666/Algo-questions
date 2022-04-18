# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

x1=35
x2=37
p1=1000000007
p2=1000000009



def precompute(H,s,m,x):
	for i in range(len(H)-1):
		H[i + 1] = ((x *H[i]) % m + ord(s[i])) % m

def computePower(power1,power2):
		for i in range(len(power1)-1):
			power1[i+1]=(power1[i]*x1)%p1
			power2[i+1]=(power2[i]*x2)%p2

def settings(s,t):
	power1 = [1] * min(len(s),len(t))
	power2 = [1] * min(len(s),len(t))

	computePower(power1,power2)

	S1 = [0] * (len(s) + 1)
	T1 = [0] * (len(t) + 1)
	precompute(S1, s, p1, x1)
	precompute(T1, t, p1, x1)

	S2 = [0] * (len(s) + 1)
	T2 = [0] * (len(t) + 1)
	precompute(S2, s, p2, x2)
	precompute(T2, t, p2, x2)
	return S1,T1,S2,T2,power1,power2

def solve(s, t,l,r,S1,T1,S2,T2,power1,power2):
	k=(l+r)//2
	po1 = power1[k]
	po2 = power2[k]
	ans=Answer(0,0,0)
	test=0

	# print(S1,T1,'\n',S2,T2)
	for i in range(0,len(t)-k+1):
		for j in range(0,len(s)-k+1):
			if (T1[i+k]-T1[i]*po1)%p1==(S1[j+k]-S1[j]*po1)%p1 and (T2[i+k]-T2[i]*po2)%p2==(S2[j+k]-S2[j]*po2)%p2:
				ans= Answer(j,i,k)
				test=1
				break
	if l==k:
		return ans
	else:
		if test==0:
			return solve(s,t,l,k,S1,T1,S2,T2,power1,power2)
		else:
			return solve(s,t,k,r,S1,T1,S2,T2,power1,power2)


for line in sys.stdin.readlines():
# for line in range(3):
	s, t = line.split()
	# s, t = input().split()
	S1, T1, S2, T2,power1,power2 = settings(s,t)
	ans = solve(s, t,0,min(len(s),len(t)),S1,T1,S2,T2,power1,power2)
	print(ans.i, ans.j, ans.len)
