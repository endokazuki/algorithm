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