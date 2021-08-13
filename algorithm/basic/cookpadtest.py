from operator import itemgetter
#多次元配列のソート

boxs=list(map(str,input().split()))
#print(boxs)
box_list=[]
for box in boxs:
    box_data=box.split(":")
    box_list.append(box_data)

#print(box_list)

truck_1=[]
truck_1_wgiht=[1,0]
truck_2=[]
truck_2_wgiht=[2,0]
truck_3=[]
truck_3_wgiht=[3,0]
truck_wgiht=[truck_1_wgiht,truck_2_wgiht,truck_3_wgiht]
#print(truck_1_wgiht,truck_2_wgiht,truck_3_wgiht)


for box in box_list:
    truck_wgiht.sort(key=itemgetter(1))
    #トラックの重さの大小をソート
    if truck_wgiht[0][0]==1:
        truck_1_wgiht[1]+=int(box[1])
        truck_1.append(box)
    elif truck_wgiht[0][0]==2:
        truck_2_wgiht[1]+=int(box[1])
        truck_2.append(box)
    elif truck_wgiht[0][0]==3:
        truck_3_wgiht[1]+=int(box[1])
        truck_3.append(box)

print(truck_1,truck_2,truck_3)

idlist_1=[]
for i in truck_1:
    idlist_1.append(i[0])
idlist_1=','.join(idlist_1)
print("truck_1:"+idlist_1)

idlist_2=[]
for i in truck_2:
    idlist_2.append(i[0])
idlist_2=','.join(idlist_2)
print("truck_2:"+idlist_2)

idlist_3=[]
for i in truck_3:
    idlist_3.append(i[0])
idlist_3=','.join(idlist_3)
print("truck_3:"+idlist_3)