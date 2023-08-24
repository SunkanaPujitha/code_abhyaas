# count how many times a number repeat
d={}
arr=eval(input("enter :"))
for k in arr:
    if k not in d:
        d[k]=1
    else:
        d[k]=d[k]+1
print(d)

# print which element repeat  max times
print("max times repeated elements:")
large=0
for j in d:
    if large <d[j]:
        large=d[j]
for i in d:
    if large==d[i]:
        print(i)
        
#print which element repeats min times
print("min times repeated elements:")
small = None
for x in d:
    if small==None:
        small = d[x]
    if small > d[x]:
        small=d[x]
for y in d:
    if small==d[y]:
        print(y)
    
