#7-A

parson=list(map(int,input().split()))
#print(parson[0],parson[1],parson[2])
#初回の入力

while parson[0]!=-1 or parson[1]!=-1 or parson[2]!=-1:
    #最終値の時、判定を終了させる
    if 80<=parson[0]+parson[1] and parson[0]!=-1 and parson[1]!=-1:
        print("A")
        parson=list(map(int,input().split()))
    elif 65<=parson[0]+parson[1]<80 and parson[0]!=-1 and parson[1]!=-1:
        print("B")
        parson=list(map(int,input().split()))
    elif 50<=parson[0]+parson[1]<65 and parson[0]!=-1 and parson[1]!=-1:
        print("C")
        parson=list(map(int,input().split()))
    elif 30<=parson[0]+parson[1]<50 and parson[0]!=-1 and parson[1]!=-1:
        if 50<=parson[2]:
            print("C")
            parson=list(map(int,input().split()))
        else:
            print("D")
            parson=list(map(int,input().split()))
    else:
        print("F")
        parson=list(map(int,input().split()))

