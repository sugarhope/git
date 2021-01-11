def binary_search(data,value):
    left=0
    right=len(data)-1
    while left<=right:
        mid=(right+left)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            left=mid+1
        elif data[mid]>=value:
            right=mid-1
    return -1

if __name__=="__main__":
    data=[10,20,30,40,50,60,70,80,90]
    print(binary_search(data,50))

