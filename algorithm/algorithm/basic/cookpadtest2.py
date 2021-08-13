import itertools
#組み合わせのパターン
from operator import itemgetter
#多次元配列のソート

#先頭結果を引き渡すAPI関数(但し、input_dataを用いて2つずつ比較した結果の結末として行え)
def api(a,b):
    #print(a,b)
    a_p=0
    b_p=0
    if a=="griffin":
        a_p=10
    elif a=="vampire":
        a_p=50
    elif a=="dragon":
        a_p=100
    elif a=="troll":
        a_p=1000
    elif a=="medusa":
        a_p=100000
    else:
        a_p=0

    if b=="griffin":
        b_p=10
    elif b=="vampire":
        b_p=50
    elif b=="dragon":
        b_p=100
    elif b=="troll":
        b_p=1000
    elif b=="medusa":
        b_p=100000
    else:
        b_p=0
    #print(a_p,b_p)

    if a_p < b_p:
        dict={"winner":b,"loser":a}
    elif b_p <a_p:
        dict={"winner":a,"loser":b}
    else:
        dict={"winner":a,"loser":b}
    return dict


input_data=list(map(str,input().split()))

monster_list=[]
for i in input_data:
    monster_data=[]
    #名前、点数
    monster_data.append(i)
    monster_data.append(0)
    monster_list.append(monster_data)
#print(monster_list)

for i in itertools.combinations(input_data,2):
    #print(i)
    #print(i[0],i[1])
    a=i[0]
    b=i[1]
    result=api(a,b)
    #print(result)
#griffin vampire dragon troll medusa
    for e,j in enumerate(input_data):
        if result["winner"]==j:
            monster_list[e][1]+=1
        elif result["loser"]==j:
            monster_list[e][1]-=1
#print(monster_list)
monster_list.sort(key=itemgetter(1),reverse=True)

#print(monster_list)
for i in monster_list:
    print(i[0])
#1行ずつ表示

result_monster=[]
for i in monster_list:
    result_monster.append(i[0])
print(*result_monster)
#1行で表示
