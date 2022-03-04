'''length of Sub Sequence
l=[5,3,1,3,3]
arr=[1,3,5]'''
n=int(input())
l=list(int(i) for i in input().split())
arr=[]
for i in l:
    if i in arr:
        break
    else:
        arr.append(i)
print(len(sorted(arr)))