import math

a,b,angle=map(int,input().split())

S=a*b*0.5*math.sin(math.radians(angle))
c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(angle)))
#余弦定理で辺の長さを求める
L=a+b+c
h=2*S/a

print('{:.5f}'.format(S))
print('{:.5f}'.format(L))
print('{:.5f}'.format(h))

#三角関数の公式
#https://atarimae.biz/archives/24942
#https://math-jp.net/2018/08/18/dai2-yogen-teiri/