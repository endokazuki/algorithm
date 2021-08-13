"""""
#バブルソート
def bubble_sort(array,lenth):
    cost=0
    for erea in range(lenth):
        for target_point in range(lenth-1, erea, -1):
            #配列の逆から行っている
            if array[target_point] < array[target_point-1]:
                array[target_point], array[target_point-1] = array[target_point-1], array[target_point]
            #右側のカードの数字が左側のカードの数字より小さい場合、カードの交換を行う
        if array[target_point]!=array[target_point-1]:
            cost+=array[target_point]+array[target_point-1]
        else:
            pass
        #入れ替えが行われた時移動コストを算出する
    return cost
"""

#選択ソート
def selection_sort(array,lenth):
    i=0
    j=i
    cost=0

    while i<=lenth-1:
        minj=i
        while j<=lenth-1:
            if array[j]<array[minj]:
                minj=j
            j+=1
        array[i],array[minj]=array[minj],array[i]
        #最小値との入れ替え（ない場合は自分自身を入れ替える）
        if array[i]!=array[minj]:
            cost+=array[i]+array[minj]
        else:
            pass
        #入れ替えが行われた時移動コストを算出する
        
        i+=1
        j=i
        #初期化
    #print(*array)
    return cost

#パーティションで左右に区切る
def partition(array, prime, last,cost):
    low_group  = prime
    for check in range(prime, last):
        if array[check]<= array[last]:
            array[low_group], array[check] = array[check], array[low_group]
            #値を小さいグループに入れ、グループからはじき出された値は後方のグループの空いた部分に入れる
            cost+=array[low_group]+array[check]
            low_group += 1
        #値の小さいグループを見つけ出し、最後にパーティションを置く領域を用意する(最後のlow_groupは値の小さいグループには所属しない)
    array[low_group], array[last] = array[last], array[low_group]
    #最後にパーティション値を、小さい値のグループと大きい値のグループにわけるように置く
    partition= low_group
    return partition,cost

#クイックソート
def quick_sort(array,prime,last,cost):

    if prime<last:
        partition_position,cost=partition(array,prime,last,cost)
        #パーティションで左右に区切る
        quick_sort(array,prime,partition_position-1,cost)
        #左側の領域をパーティションを用いたソートする
        quick_sort(array,partition_position+1,last,cost)
        #右側の領域をパーティションを用いたソートする
    return cost


lenth=int(input())
#配列数
array = list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方
selection_array=array
quick_array=array


selection_sort_cost=selection_sort(selection_array,lenth)
quick_sort_cost=quick_sort(array,0,lenth-1,0)

print(selection_sort_cost,quick_sort_cost)

if selection_sort_cost<=quick_sort_cost:
    print(selection_sort_cost)
else:
    print(quick_sort_cost)
#コスト数の少ないソートを表示する