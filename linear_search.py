#linear search
arr=eval(input("enter:"))
target=int(input("target:"))
found_index=-1
for i in range(len(arr)):
    if arr[i]==target:
        found_index=i
        break;
if found_index!=-1:
    print("target is found at index ",found_index)
else:
    print("target is not found")
    
    
