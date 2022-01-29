ms= [
	 [8, 4, 4],
	 [1, 5, 9],
	 [6, 7, 2]
]
i=0
row1=0
row2=0
row3=0
cs1=0
cs2=0
cs3=0	
ds1=0
ds2=0
ds3=0
while i<len(ms):
	row1=row1+ms[i][0]
	row2=row2+ms[i][1]
	row3=row3+ms[i][2]
	cs1=cs1+ms[i][0]
	cs2=cs2+ms[i][1]
	cs3=cs3+ms[i][2]
	ds1=ds1+ms[i][0]
	ds2=ds2+ms[i][1]
	ds3=ds3+ms[i][2]
	i+=1    
print ("total row1",row1)
print ("total row2",row2)
print ("total row3",row3)
print("total c1",cs1)
print("total c2",cs2)
print("tootal c3",cs3)
print("total ds1",ds1)
print("total ds2",ds2)
print("total ds3",ds3)