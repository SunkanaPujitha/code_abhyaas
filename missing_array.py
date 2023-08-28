# for single missing element
n=int(input("enter:"))
arr=eval(input("enter:"))
sum1=(n*(n+1))//2
for i in arr:
    sum1=sum1-i
print(sum1)

#for multiple
arr=eval(input("enter:"))
n=int(input("enter range:"))
for i in range(1,n+1):
    if i not in arr:
        print(i)
     
        
