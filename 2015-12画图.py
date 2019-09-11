#-*- coding: utf-8 -*-
m,n,q = list(map(int,input().split()))  #m¿ín¸ß
actions = []
for i in range(q):
	actions.append(input().split())
photo = [['.']*m for i in range(n)]
def fill_photo(x,y,sym):
	photo[n-1-y][x] = sym
	if n-1-y-1 >= 0 and photo[n-1-y-1][x] not in [sym,'|','+','-']:  #up
		fill_photo(x,y+1,sym)
	if n-1-y+1 <= n-1 and photo[n-1-y+1][x] not in [sym,'|','+','-']:  #dowm
		fill_photo(x,y-1,sym)
	if x-1 >= 0 and photo[n-1-y][x-1] not in [sym,'|','+','-']:  #left
		fill_photo(x-1,y,sym)
	if x+1 <= m-1 and photo[n-1-y][x+1] not in [sym,'|','+','-']:  #right
		fill_photo(x+1,y,sym) 

for act in actions:
	if act[0] == '0':
		x1,y1,x2,y2 = list(map(int,act[1:]))
		if x1 == x2: #»­ÊúÏß
			for i in range(min(y1,y2),max(y1,y2)+1):
				if photo[n-1-i][x1] in ['-','+']:
					photo[n-1-i][x1] = '+'
				else:
					photo[n-1-i][x1] = '|'
		else:         #»­ºáÏß
			for i in range(min(x1,x2),max(x1,x2)+1):
				if photo[n-1-y1][i] in ['-','+']:
					photo[n-1-y1][i] = '+'
				else:
					photo[n-1-y1][i] = '-'
	else:  #Ìî³ä
		x1,y1 = list(map(int,act[1:3]))
		sym = act[3]
		fill_photo(x1,y1,sym)
for i in photo:
	for j in i:
		print(j,end='')
	print('\n',end='')