arr=eval(input("enter:"))
max1=float('-inf')
max2=float('-inf')
min1=float('inf')
min2=float('inf')
print("second largest:")
for i in range(len(arr)):
    if(max1<arr[i]):
        max2=max1
        max1=arr[i]
    if(arr[i]>max2 and arr[i]!=max1):
        max2=arr[i]
print(max2)
print("second smallest:")
for j in range(len(arr)):
    if(min1>arr[j]):
        min2=min1
        min1=arr[j]
     if(arr[j]<min2 and arr[j]!=min1):
        min2=arr[j]
print(min2)

