a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
b=[23,19,15,25,31,43,9]
c=[14,12,42,56]
sum=0
sum1=0
ave=0
ave1=0
while index<(len(a)):
    if a[index]%2==0:
        sum=sum+(a[index])
        ave=sum/len(c)
    else:
        sum1=sum1+(a[index])
        ave1=sum1/len(b)
    index=index+1
print("total ave", ave)
print("total ave",ave1)    