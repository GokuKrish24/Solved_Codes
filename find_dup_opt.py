L=[3,1,3,4,2]
s=L[0]
f=L[0]
while(True):
    s=L[s]
    f=L[L[f]]
    if(s==f):
        break
f=L[0]
while(f!=s):
    f=L[f]
    s=L[s]
print(s)
