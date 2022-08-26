import math
List_1=[8,2,3,4,7,5,20,8,5,10,11,12,2,14,15,2,14,3,4,1]
List_2=[]

for number in range(len(List_1)):
    List_2.append(math.pow(List_1[number],2))

print('numbers=',List_1)
print('........................')
print('numbers to the power two=',List_2)

