S=str(input())
week=['MON','TUE','WED','THU','FRI','SAT','SUN']
ans=week.index('SUN')-week.index(S)
if ans==0:
    ans=7
print(ans)