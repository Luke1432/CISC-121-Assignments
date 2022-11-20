l=[1676, 267, 100, 3];
index=0;
sortedIndex=0;
min=l[0]

for k in range(len(l)-1):
    for i in range(sortedIndex, len(l)):
        if l[i] < min: min = l[i]; index = i
    for j in range(index, sortedIndex, -1): l[j]=l[j-1]
    sortedIndex+=1; l[sortedIndex-1]=min; min=l[sortedIndex]
print(l)

