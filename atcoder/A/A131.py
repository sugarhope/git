S=str(input())
i=''
ans=''
for s in S:
    if s==i:
        ans='Bad'
        break
    else:
        i=s
if ans=='':
    ans='Good'
print(ans)