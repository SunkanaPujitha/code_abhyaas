# which element appears one time only
arr=eval(input("enter:"))
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for j in d:
    if d[j]==1:
        print(j)
        
