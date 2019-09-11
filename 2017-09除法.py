n,m = list(map(int,input().split()))
num = list(map(int,input().split()))
for i in range(m):
	x = list(map(int,input().split()))
	if x[0] == 1:
		l,r,v = x[1:]
		for j in range(l-1,r):
			if num[j] % v == 0:
				num[j] = num[j] // v
	else:
		l,r = x[1:]
		print(sum(num[l-1:r]))