#6-1
lenth=int(input())
array=list(map(int,input().split()))
reversed_array=[]

for index in reversed(array):
    reversed_array.append(index)
#配列を反転して出力を行う

print(*reversed_array)

#番外
lenth=int(input())
array=list(map(str,input().split()))
array_point=0
print(array[array_point])
check=""

while array_point<=lenth-3:
    if array[array_point]=="A" and array[array_point+1]=="A" and array[array_point+2]=="G":
        check="true"
    else:
        pass
    array_point+=1
#配列にAAGがあるか否かを検証

if check=="true":
    print(array)
else:
    pass

#6-2
total_number= int(input())
#空白区切りで入れた引数を配列に保存する
#二次元配列を入力
#第一座標：カードの位置、第二座標：0=トランプの絵札,1=トランプの数字
#1次元配列では1枚のトランプのカードとして表示される（二次元配列だと第一座標を示す）
#Excelの資料を参考
#https://qiita.com/muchosucho/items/08ccf26aa77a84678f9a
#print(A[0],A[0][0],A[0][1],A[1],A[1][0],A[1][1])
#H4 H 4 C9 C 9
origin_card_box=[]
card_box=[]


#全てのトランプを箱に収める
pattern_count=0
number_count=0
while pattern_count<=4-1:
    pattern=['S','H','C','D']
    while number_count<=13-1:
        number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        card=[]
        card.append(pattern[pattern_count])
        card.append(number[number_count])
        origin_card_box.append(card)
        number_count+=1
    number_count=0
    pattern_count+=1
#print(origin_card_box)
#print(origin_card_box[52-1])
#print(len(origin_card_box))

count=0
#存在するトランプを箱に収める
while count<=total_number-1:
    card=[]
    pattern,number=input().split()
    number=int(number)
    card.append(pattern)
    card.append(number)
    #print(card)
    #print(type(card))
    card_box.append(card)
    #print(card_box[0][0],card_box[0][1])
    count+=1
#print(card_box)

#存在するカードはリストから除外する
for index in card_box:
    origin_card_box.remove(index)
    #remove:配列内の指定の要素の削除


#存在しないカードを出力する
for index in origin_card_box:
    print(*index)

#6-3

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

#6-4
n,m=input().split()
n=int(n)
m=int(m)
#1×m,n×m

#aの初期行列の作成
a=[]
for hight in range(n):
    column=[]
    a.append(column)

#bの初期行列の作成
b=[]
for hight in range(m):
    column=[]
    b.append(column)

#計算結果用の初期行列の作成
#n行m列×m行1列＝n行1列
result=[]
for hight in range(n):
    column=[]
    result.append(column)

#print(a)
#print(b)

#aの行列
for hight in range(n):
    num=list(map(int,input().split()))
    for width in range(m):
        a[hight].append(num[width])
#print(a)

#bの行列
for hight in range(m):
    num=int(input())
    b[hight].append(num)
#print(b)

##計算結果用の行列の作成
#n行m列×m行1列＝n行1列
for n_num in range(n):
    sum=0
    for m_num in range(m):
        #print(a[n_num][m_num],b[m_num][0])
        sum+=a[n_num][m_num]*b[m_num][0]        
    result[n_num].append(sum)
#print(result)

for out_put in range(n):
    print(*result[out_put])

