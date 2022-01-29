# i=1
# while i<=100:
#     j=2
#     count=0
#     while j<i:
#         if i%j==0:
#             count=count+1
#         j=j+1

#     if count==0:
#         print(i,"prime")
#     i+=1



# a=['red', 'white', 'a', 'b', 'black', 'f']
# i=0
# string= ""
# while i<len(a):
#     string=string+(a[i])
#     # print(string)
#     string.split(a[i])
#     i=i+1
# print(string)


# a= ["red","white","a","black","f" ]
# i=0
# string=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         string=string+(a[i][j])
#         j+=1
#     i+=1
# print(string)


# a=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
# i=0
# b=[]
# while i<len(a):
# 	if type(a[i])==type([]):
# 		j=0
# 		while j<len(a[i]):
# 			if type(a[i][j])==type([]):
# 				k=0
# 				while k<len(a[i][j]):
# 					b.append(a[i][j][k])
# 					k+=1
# 			else:
# 				b.append(a[i][j])
# 			j+=1
# 	else:
# 		b.append(a[i])
# 	i+=1
# print(b)


# name=input("enter any name....")
# str=""
# i=0
# while i<len(name):
#     if name[i]=='a'or name[i]=='e'or name[i]=='i'or name[i]=='o'or name[i]=='u':
#        pass
#     else:
#         str=str+name[i]
#     i=i+1
# print(str)


# list=[11,33,55]
# def show():
#  string=""
#  i=0
#  while i<len(list):
#    string=string+str(list[i])
#    i=i+1
#  print(string)
# show()


# a=["manpreet"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)


# a=[1,2,[3,4,5],[1,2],[7,8],9,[2,3,4]]
# i=0
# b=[]
# while i<len(a):
# 	if type(a[i])==type([]):
# 		j=0
# 		while j<len(a[i]):
# 			if type(a[i][j])==type([]):
# 				k=0
# 				while k<len(a[i][j]):
# 					b.append(a[i][j][k])
# 					k+=1
# 			else:
# 				b.append(a[i][j])
# 			j+=1
# 	else:
# 		b.append(a[i])
# 	i+=1
# print(b)



# a=[12,67,98,34]
# i=0
# while  i<len(a):



# a=[12,67,98,34]
# sum=0
# i=0
# while i<len(a):
#     k=a[i]%10
#     k1=a[i]//10
#     k2=a[i]/10
#     sum=k+k1
#     print(sum,end=" ")
#     i=i+1


# a=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i+=1
# print(b)


# a=[1,2,3,4,5,6,7,8]
# i=0
# d=[]
# c=a[i]
# while i<len(a)-1:
# 	c=a[i+1]
# 	b=str(a[i]+c)
# 	d.append(b)
# 	i+=1
# print(d)

# a=[1,2,3,4,5,6,7,8]
# i=0
# d=[]
# c=a[i]
# while i<len(a)-1:
# 	c=a[i+1]
# 	b=str(a[i]+c)
# 	d.append(b)
# 	i+=1
# print(d)


a=[1,2,3,4,5,6]
i=0
while i<len(a):
    print(i+1)
i+=2