'''
5 4
/articles/2003/ special_case_2003
/articles/<int>/ year_archive
/articles/<int>/<int>/ month_archive
/articles/<int>/<int>/<str>/ article_detail
/static/<path> static_serve
/articles/2004/
/articles/1985/09/aloha/
/articles/hello/
/static/js/jquery.js
'''
n, m = list(map(int,input().split()))
nn = []
mm = []
for i in range(n):
	nn.append(input())
for j in range(m):
	mm.append(input())
name = [i.split()[1] for i in nn]
nn = [i.split()[0] for i in nn]
nn = [i.split('/') for i in nn]
mm = [i.split('/') for i in mm]
#[['articles', '2003', ''], ['articles', '<int>', ''], ['articles', '<int>', '<int>', ''], ['articles', '<int>', '<int>', '<str>', ''], ['static', '<path>']] 
#[['articles', '2004', ''], ['articles', '1985', '09', 'aloha', ''], ['articles', 'hello', ''], ['static', 'js', 'jquery.js']]

for mat in mm:
	if_found = False
	for rule in nn:
		arg = []
		match = 0
		path_match = False
		if len(mat) >= len(rule):
			for j in range(len(rule)):
				if rule[j] == mat[j]:
					match+=1
				elif rule[j] == '<int>' and mat[j].isdigit():
					match+=1
					arg.append(int(mat[j]))
				elif rule[j] == '<str>' and mat[j] != '':
					match+=1
					arg.append(mat[j])
				elif rule[j] == '<path>':
					match+=1
					path_match = True
					arg.append('/'.join(mat[j:]))
				else:
					break
		if match == len(rule) and (len(rule) == len(mat) or path_match == True):
			if_found = True
			print(name[nn.index(rule)]+' '+' '.join(map(str,arg)))
			break
	if if_found == False:
		print('404')