X=int(input())
ans=0
temp=0

if X % 100 == 0:
    ans=100
else:
    temp = X % 100
    ans = 100 - temp

print(ans)