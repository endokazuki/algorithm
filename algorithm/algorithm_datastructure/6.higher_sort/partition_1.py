lenth=int(input())
#配列数
array = list(map(int, input().split()))

partiton_index=array[-1]
#パーティションを行う数を取得する
#print(partiton_index)

array_point=0
array_under=[]
array_over=[]

while array_point<=len(array)-2:
    #最後の配列の数はパーティションのため、比較を行わない
    if array[array_point]<=partiton_index:
        array_under.append(array[array_point])
    else:
        array_over.append(array[array_point])
    array_point+=1
    #パーティション値の比較を行う

print(*array_under,"["+str(partiton_index)+"]",*array_over)

array=[]
#arrayの初期化
for index in array_under:
    array.append(index)
array.append(partiton_index)
for index in array_over:
    array.append(index)
print(array)
#パーティション後の配列を配備