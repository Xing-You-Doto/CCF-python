n = int(input())
num = list(map(int,input().split()))
res = []
for i in range(n):
	width = 0
	for j in reversed(range(i)):
		if num[j] >= num[i]:
			width+=1
		else:
			break
	for k in range(i,n):
		if num[k] >= num[i]:
			width+=1
		else:
			break
	res.append(num[i]*width)   #比使用max迭代快 50+ms
print(max(res))