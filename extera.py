a=[[1,2,3],[4,5,6],[7,8,9],[5,8]]
i=0
b=[]
while i<len(a):
	if type(a[i])==type([]):
		j=0
		while j<len(a[i]):
			if type(a[i][j])==type([]):
				k=0
				while k<len(a[i][j]):
					b.append(a[i][j][k])
					k+=1
			else:
				b.append(a[i][j])
			j+=1
	else:
		b.append(a[i])
	i+=1
print(b)
