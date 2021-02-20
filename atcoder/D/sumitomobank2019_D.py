N=int(input())
S=str(input())

count=0

for i in range(1000):
    s=str(i).zfill(3)
    now = 0

    for j in S:
        if j == s[now]:
            now+=1
        if now==3:
            count+=1
            break
print(count)