#-*- coding:utf-8 -*-
'''
3
crm:2
git:3
game
4
hr 1 crm:2
it 3 crm:1 git:1 game
dev 2 git:3 game
qa 1 git:2
3
alice 1 hr
bob 2 it qa
charlie 1 dev
9
alice game
alice crm:2
alice git:0
bob git
bob poweroff
charlie game
charlie crm
charlie git:3
malice game
'''
p = int(input())
power = {}
for i in range(p):
	mm = input().split(':')
	if len(mm) > 1:
		power[mm[0]] = int(mm[1])
	else:
		power[mm[0]] = -1	
r = int(input())
actor = {}
for i in range(r):
	mm = input().split()
	actor[mm[0]] = mm[2:]
u = int(input())
body = {}
for i in range(u):
	mm = input().split()
	body[mm[0]] = mm[2:]
for name in body.keys():
	ll = body[name]
	nn = []
	for i in ll:
		nn.extend(actor[i])
	body[name] = nn
q = int(input())
for i in range(q):
	name,pp = input().split()
	dd = []
	if name in body.keys():
		dd = body[name]
	found = False
	num = -1
	for i in dd:
		if ':' in pp:  #带等级查询
			if ':' in i:
				if i[:-2] == pp[:-2] and int(i[-1]) >= int(pp[-1]):
					found = True
					break
		else:
			if i == pp:   #不分等级权限查询
				found = True
				break
			elif i[:-2] == pp:   #分等级权限的不带等级查询
				num = max(num,int(i[-1]))
				found = True
	if num != -1:
		print(num)
	elif found == True:
		print('true')
	else:
		print('false')