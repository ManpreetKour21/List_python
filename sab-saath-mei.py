a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=[14,56,12,42]
c=[23,19,9,15,25,31,43]
index=0
sum=0
sum1=0
ave=0
ave1=0
while index<(len(a)):
    if a[index]%2==0:
        print(a[index],"even")
        sum=sum+a[index]
        ave=sum/len(b)
    else:
        print(a[index],"odd")
        sum1=sum1+a[index]
        ave1=sum1/len(c)
    index=index+1
print(sum)
print(sum1)
print(ave,"ave of even numbers")
print(ave1,"ave of odd numbers")