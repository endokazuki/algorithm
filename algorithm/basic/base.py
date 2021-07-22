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

#Q11
while True:
    a,b=map(int,input().split())
    if a < b:
        print(a,b)
    elif a > b:
        print(b,a)
    else:
        print(a,b)

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