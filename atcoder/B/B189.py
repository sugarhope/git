N,X=map(int,input().split())
VP=[list(map(int,input().split())) for _ in range(N)]

alco=0
count=[]
for i in range(0,N):
    alco+=(VP[i][0]*VP[i][1]/100)
    if alco > X:
        count.append(i+1)
if count==[]:
    print(-1)
else:
    print(min(count))