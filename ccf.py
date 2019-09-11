#-*- coding: utf-8 -*-
n = int(input())
num = list(map(int,input().split()))
num.sort()
a = n // 2
b = (n-1) // 2
x = y = 1
while b-x >= 0:
	if num[b-x] != num[b]:
		break
	else:
		x += 1
while a+y <= n-1:
	if num[a+y] != num[a]:
		break
	else:
		y += 1
if x == y and num[a] == num[b]:
	print(num[a])
else:
	print(-1)