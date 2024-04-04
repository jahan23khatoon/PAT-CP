#find kth smallest element of list
import heapq
def find_klarge(arr):
    arr=[-item for item in arr]
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s*-1
arr=list(map(int,input("enter:").split()))
k=int(input("enter values:"))
ans=find_klarge(arr,k)
print(ans)
