#Q1
print("Hello World")

#Q2
x = input()
y = int(x)**3
print (y)

#Q3
#及第点
a=input()
b=input()
rectangle_area=int(a)*int(b)
rectangle_side=2*int(a)+2*int(b)
print(rectangle_area,rectangle_side)
#TLE (Time Limit Exceeded)する

#正解
c,d = map(int,input().split())
#map関数：
# 第1引数は関数（上記の場合ではint関数[変数を数値型に変換する]）
# 第2引数は導入する変数
# input().split():Pythonで複数の文字列を入力する方法
print(c*d,2*(c+d))

#Q4
q = 10 // 3
#商
mod = 10 % 3
#余り
print(q, mod)

S=input()
hour=int(S) // 3600
hour_mod=int(S) % 3600
minute=hour_mod // 60
minute_mod=hour_mod % 60
second=minute_mod
print(int(hour),int(minute),int(second),sep=':')
#seq:出力結果の間に挟むものを示す

#Q5
e,f = map(int,input().split())
#a=e,b=f
if e < f:
    print("a < b")
elif e > f:
    print("a > b")
else:
    print("a == b")

#Q6
g,h,i = map(int,input().split())
if g<h<i:
    print("Yes")
else:
    print("No")

#Q7
a,b,c=map(int,input().split())
numlist=[a,b,c]
newnumlist=sorted(numlist)
print(newnumlist[0],newnumlist[1],newnumlist[2])

#Q8
W,H,x,y,r=map(int,input().split())

#rectangle_area1=[0,0]
#rectangle_area2=[W,0]
#rectangle_area3=[W,H]
#rectangle_area4=[0,H]
#circle_center=[x,y]
circle_area1=[x,y+r]
circle_area2=[x+r,y]
circle_area3=[x-r,y]
circle_area4=[x,y-r]

circle_area=[x+r,y+r,x-r,y-r]

if circle_area1[1] <= H and circle_area2[0]<= W and 0 <=circle_area3[0] and 0 <= circle_area4[1]:
    print("Yes")
else:
    print("No")

#Q9
x=1
while x<=1000:
    print("Hello World")
    x+=1

#Q10
num = 1
while True:
#無限ループ
    x = int(input())
    if x == 0: break
    print ("Case {0}: {1}".format(num,x))
    #変数をいれる位置を決める
    num += 1

"""""
#Q11
while True:
    a,b=map(int,input().split())
    if a < b:
        print(a,b)
    elif a > b:
        print(b,a)
    else:
        print(a,b)
"""""

#Q13
a,b,c=map(int,input().split())
count=int(0)
while a<=b:
    mod=c%a
    if mod==0:
        count+=1
    a+=1
print(count)

#Q14
a,b=map(int,input().split())
d=a // b
r=a % b
f_before=float(a/b)
f='{:.5f}'.format(f_before)
#浮動小数点第5位まで表示
print(d,r,f)

#3-4
a=1
b=1
big_array=[]

while a!=0 or b!=0:
    array=[]
    a,b=map(int,input().split())
    if a<b:
        array.append(a)
        array.append(b)
        big_array.append(array)
       
    else:
        array.append(b)
        array.append(a)
        big_array.append(array)

big_array.pop(-1)
#0 0の表記を削除

for out_put in big_array:
    print(*out_put)

#4-2
import math

r=float(input())

circle_area=r*r*math.pi
circumference=2*r*math.pi

circle_area='{:.5f}'.format(circle_area)
circumference='{:.5f}'.format(circumference)

print(circle_area,circumference)

#4-3
import math 

operator=""
result_array=[]

while operator!="?":
    a,operator,b=map(str,input().split())
    a=int(a)
    b=int(b)
    #print(type(a),type(operator),type(b))
    if operator=="+":
        result=a+b
        result_array.append(result)
    elif operator=="-":
        result=a-b
        result_array.append(result)
    elif operator=="*":
        result=a*b
        result_array.append(result)
    elif operator=="/" and b!=0:
        #割り算は0の割り算を許可しない
        result=a/b
        result=math.floor(result)
        #商は小数点以下を切り捨てる
        result_array.append(result)
        
for out_put in result_array:
    print(out_put)



#4-4
lenth=int(input())
array=map(int,input().split())

min=1000000
max=-1000000
sum=0

for index in array:
    if max<=index:
        max=index

    if index<=min:
        min=index

    sum+=index

print(min,max,sum)

#5-1
H,W=map(int,input().split())

while H!=0 or W!=0:
    shape=""
    while 0<W:
        shape+="#"
        W-=1
    while 0<H:
        print(shape)
        H-=1
    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する

#5-2
H,W=map(int,input().split())

while H!=0 or W!=0:
    shape=""
    #外側の図形
    shape_index=""
    #内側の図形
    while 0<W:
        shape+="#"
        if shape=="#" or W==1:
            #一番初めと一番最後（図形の外側に相当する部分）に実行
            shape_index+="#"
        else:
            shape_index+="."
        W-=1
    
    print(shape)
    while 1<H-1:
        print(shape_index)
        H-=1
    print(shape)
    #図形の作成


    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する

#5-3
H,W=map(int,input().split())

while H!=0 or W!=0:
    w_sum=W
    switch="off"
    while 0<H:
        W=w_sum
        shape=""
        set_shape=""
        #初期化する値
        
        if switch=="off":
            while 0<W:
                if set_shape=="" or set_shape==".":
                    set_shape="#"
                else:
                    set_shape="."
                shape+=set_shape
                W-=1
            print(shape)
            #奇数部分の図形の描写
            switch="on"
        elif switch=="on":
            while 0<W:
                if set_shape=="" or set_shape=="#":
                    set_shape="."
                else:
                    set_shape="#"
                shape+=set_shape
                W-=1
            print(shape)
            #偶数部分の図形の描写
            switch="off"
        H-=1
    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する

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