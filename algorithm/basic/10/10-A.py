x_1,y_1,x_2,y_2=map(float,input().split())

x_distance=x_1-x_2
y_distabce=y_1-y_2
distance=(x_distance**2+y_distabce**2)**0.5
#三角関数を用いて距離を求める
print('{:.5f}'.format(distance))
