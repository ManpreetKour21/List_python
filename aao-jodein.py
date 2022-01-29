a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
sum=0
sum1=0
while index<(len(a)):
    if a[index]%2==0:
        # print(a[index],"even")
        sum=sum+(a[index])
        # print(sum,"even")
    if a[index]%2!=0:
        # print(a[index],"odd")
        sum1=sum1+(a[index])
        # print(sum1,"odd")
    index=index+1
print(sum)
print(sum1)    