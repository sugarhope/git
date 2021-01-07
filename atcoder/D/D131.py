N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]
import operator
AB=sorted(AB,key=operator.itemgetter(1))
a=0
b=0
ans=''
for i in AB:
    a+=i[0]
    if a>i[1]:
        ans='No'
if ans=="":
    ans='Yes'
print(ans)