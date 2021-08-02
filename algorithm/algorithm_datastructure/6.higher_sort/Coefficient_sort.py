lenth=int(input())
#配列数
array = list(map(int, input().split()))
#配列数内の値
#範囲0～10000
big_array=[0]*(10000+1)
result_array=[]
#各数のカウンター

for index in array:
    big_array[index]+=1

#print(big_array)

big_array_point=0
while big_array_point<=len(big_array)-1:
    while big_array[big_array_point]!=0:
        result_array.append(big_array_point)
        big_array[big_array_point]-=1
    #各数字でカウンターの数が存在する場合、カウンターが0になるまで該当の数を出し続ける
    big_array_point+=1

print(*result_array)