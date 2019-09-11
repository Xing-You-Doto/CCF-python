action = []
n = int(input())
for i in range(n):
	x = list(input().split())
	action.append(x)
player1 = {'HP':30,'master_num':0,'master_HP':[]}
player2 = {'HP':30,'master_num':0,'master_HP':[]}
play = [player1,player2]
time = 0
for act in action:
	time2 = (time+1)%2
	if act[0] == "summon":
		pos,attack,HP = list(map(int,act[1:]))
		play[time]['master_HP'].insert(pos-1,[attack,HP])
	elif act[0] == "attack":
		a,b = int(act[1]),int(act[2])
		if b == 0:  #攻击对方英雄
			play[time2]['HP'] -= play[time]['master_HP'][a-1][0]
			if play[time2]['HP'] <= 0:
				break    #英雄死亡造成结束
		else:   #随从攻击随从
			play[time]['master_HP'][a-1][1] -= play[time2]['master_HP'][b-1][0]
			play[time2]['master_HP'][b-1][1] -= play[time]['master_HP'][a-1][0]
			if play[time]['master_HP'][a-1][1] <= 0:
				del  play[time]['master_HP'][a-1]
			if play[time2]['master_HP'][b-1][1] <= 0:
				del play[time2]['master_HP'][b-1]
	else:  #end
		time = (time+1)%2
if play[0]['HP']  <= 0:
	print(-1)
elif play[1]["HP"] <= 0:
	print(1)
else:
	print(0)
print(play[0]['HP'])
a = [len(play[0]['master_HP'])]
for i in range(a[0]):
	a.append(play[0]['master_HP'][i][1])
print(' '.join(map(str,a)))
print(play[1]['HP'])
a = [len(play[1]['master_HP'])]
for i in range(a[0]):
	a.append(play[1]['master_HP'][i][1])
print(' '.join(map(str,a)))
