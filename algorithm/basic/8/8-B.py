#8-B
num=str(input())

while num!="0":
    sum=0
    for i in range(len(num)):
        sum+=int(num[i])
    print(sum)
    num=str(input())

