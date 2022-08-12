list1=[2,7,11,15]
list2=[]
val=9
for i in list1:
    for j in list1:
        if i+j==val:
            list2.append(list1.index(i))
            list2.append(list1.index(j))
print(list(set(list2)))