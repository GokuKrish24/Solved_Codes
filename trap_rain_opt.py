arr=[1,0,0,0,0,1]
l=0
left=0
r=len(arr)-1
right=0
ans=0
while(l<r):
    if(arr[l]<arr[r]):
        if(left<arr[l]):
            left=arr[l]
        else:
            ans+=left-arr[l]
        l+=1
    else:
        if(right<=arr[r]):
            right=arr[r]
        else:
            ans+=right-arr[r]
        r-=1
print(ans)