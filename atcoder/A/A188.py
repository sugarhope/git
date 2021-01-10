XY=list(map(int,(input().split())))
sa=max(XY)-min(XY)
if sa<3:
    print('Yes')
else:
    print('No')