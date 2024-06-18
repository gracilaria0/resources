with open('./作业.md', 'r', encoding='utf-8') as zy:
	zylines = zy.readlines()
	for i in range(len(zylines)):
		if zylines[i].startswith('#### '):
			nf = open('./作业/' + zylines[i][5:-1] + '.md', 'w', encoding='utf-8')
			while not zylines[i].startswith('---'):
				nf.write(zylines[i])
				i = i + 1
