from scipy.spatial import distance
N,D=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(N)]
count=0
for i in range(0,N):
    for j in range(i+1,N):
        ans=distance.euclidean(x[i],x[j])
        ans=str(ans)       
        if ans[-1]=='0':
            count+=1
print(count)