A,B,C,X,Y=map(int,input().split())

ans=0
if (A+B)<=C*2:
    ans=A*X+B*Y
else:
    temph=C*max(X,Y)*2
    if X<=Y:
        tempab=C*min(X,Y)*2+B*(Y-X)
    elif X>Y:
        tempab=C*min(X,Y)*2+A*(X-Y)
    ans=min(temph,tempab)
print(ans)