import xlrd
path=("./everyone.xlsx")
x=xlrd.open_workbook(path)
sheet = x.sheet_by_index(0)
name=[None]*250;
rollno=[None]*250;
namematch=[0]*250
def match(worda,wordb,index):
	for y in wordb.split():
		for x in worda.split():
			if x.lower() == y.lower():
				namematch[index]+=1;
roll=input("enter name/rollno: ")
bestmatch=0
for i in range(216):
	name[i]=sheet.cell_value(i,0)
	rollno[i]=str(sheet.cell_value(i,1))
	rollno[i]=(rollno[i])[:-2]
	if rollno[i] == roll:
		print(name[i])
		exit()
for i in range(216):
	name[i]=sheet.cell_value(i,0)
	rollno[i]=str(sheet.cell_value(i,1))		
	rollno[i]=(rollno[i])[:-2]
	match(name[i],roll,i)
mx=0;uniq=0
for i in range(216):
	if mx < namematch[i]:
		mx=namematch[i]
		bestmatch=i
for i in range(216):
	if namematch[i] == namematch[bestmatch]:
		uniq+=1
if namematch[bestmatch]==0:
	print("no matches found")
	exit()	
if bestmatch > 0:
	print(name[bestmatch]+'\t'+rollno[bestmatch])	
choice='n'
if uniq > 1:
	choice=input("show other matches? y/n: ")
for i in range(216):
	if namematch[i] == namematch[bestmatch] and i != bestmatch and choice=='y':
		print(name[i]+'\t'+rollno[i])	
