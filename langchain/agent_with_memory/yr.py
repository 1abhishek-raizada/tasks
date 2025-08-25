
list=[8,7,2,1]
maxe=0
left=0
right=len(list)-1
while left < right:
    height=min(list[left],list[right])
    width=right-left
    maxe=max(maxe,height*width)
    if list[left]<list[right]:
        left+=1
    else:
        right-=1   