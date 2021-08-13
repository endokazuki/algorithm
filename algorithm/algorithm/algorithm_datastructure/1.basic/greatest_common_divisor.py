
#正しいが、計算量が足りない
a,b=map(int,input().split())
if a<b:
    a,b=b,a
#後の計算量を減らすため、a<bと定義する
divisor_a=[]
divisor_b=[]
num_a=1
num_b=1

while num_a<=a:
    result_a=a % num_a
    if result_a ==0:
        divisor_a.append(num_a)
    else:
        pass
    num_a+=1
#aの約数を求める
while num_b<=b:
    result_b=b % num_b
    if result_b ==0:
        divisor_b.append(num_b)
    else:
        pass
    num_b+=1
#bの約数を求める

point_a=-1
point_b=-1
#配列の最後尾（各約数の最大値からスタート）

#print(divisor_a[-(len(divisor_a))])
#配列の先端を表示
#print(divisor_a,divisor_b)


while divisor_b[point_b]!=divisor_a[point_a]:
#print(point_a,point_b)
    point_a-=1
    if point_a==-(len(divisor_a)):
        point_a=-1
        #対象の約数の位置を最後尾に戻す
        point_b-=1
        #対抗の約数のポイントを１つ「前」にずらす
    if divisor_b[point_b]==1:
        break
    #最大公約数が１の時（公約数が１つしか存在しない時）、結果を「１」として終了
print(divisor_b[point_b])
#最大公約数地点の結果を出力

#模範解答
a, b = map(int, input().split())
if a < b:
  a, b = b, a
while b != 0:
  a, b = b, a % b
print(a)