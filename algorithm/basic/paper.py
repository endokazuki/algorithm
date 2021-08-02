#6-3

#賢い回答は3次元配列を利用している
building_1=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
building_2=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
building_3=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
building_4=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

result=[]

input_data=int(input())
for num in range(input_data):
    building,floor,room,number=map(int,input().split())
    if building==1:
        building_1[room-1][floor-1]+=number
    if building==2:
        building_2[room-1][floor-1]+=number
    if building==3:
        building_3[room-1][floor-1]+=number
    if building==4:
        building_4[room-1][floor-1]+=number
    

#b2=[[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

first=[]
for room in range(0,10):
    index=building_1[room][0]
    first.append(index)
    
second=[]
for room in range(0,10):
    index=building_1[room][1]
    second.append(index)


third=[]
for room in range(0,10):
    index=building_1[room][2]
    third.append(index)

"""""
print(*first)
print(*second)
print(*third)
print("#"*20)
"""""

result.append(first)
result.append(second)
result.append(third)
result.append("#"*20)


first=[]
for room in range(0,10):
    index=building_2[room][0]
    first.append(index)
    
second=[]
for room in range(0,10):
    index=building_2[room][1]
    second.append(index)


third=[]
for room in range(0,10):
    index=building_2[room][2]
    third.append(index)

result.append(first)
result.append(second)
result.append(third)
result.append("#"*20)

first=[]
for room in range(0,10):
    index=building_3[room][0]
    first.append(index)
    
second=[]
for room in range(0,10):
    index=building_3[room][1]
    second.append(index)


third=[]
for room in range(0,10):
    index=building_3[room][2]
    third.append(index)

result.append(first)
result.append(second)
result.append(third)
result.append("#"*20)

    
first=[]
for room in range(0,10):
    index=building_4[room][0]
    first.append(index)
    
second=[]
for room in range(0,10):
    index=building_4[room][1]
    second.append(index)


third=[]
for room in range(0,10):
    index=building_4[room][2]
    third.append(index)

result.append(first)
result.append(second)
result.append(third)

for index in result:
    if type(index) is list:
        print(*index)
    else:
        print(index)