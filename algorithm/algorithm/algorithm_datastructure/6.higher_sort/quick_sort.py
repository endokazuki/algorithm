def bubble_sort(bubble_array,lenth):
    #バブルソート
    for erea in range(lenth):
        for target_point in range(lenth-1, erea, -1):
            #配列の逆から行っている
            if bubble_array[target_point][1] < bubble_array[target_point-1][1]:
                bubble_array[target_point], bubble_array[target_point-1] = bubble_array[target_point-1], bubble_array[target_point]
            #右側のカードの数字が左側のカードの数字より小さい場合、カードの交換を行う
        #print(*card_box)
    #1周すると左端の領域が確定し、その右隣の領域の検証を開始する（これを配列が終わるまで繰り返す）
    #print(*bubble_array)
    #print("Stable")
    #バブルソートは常に安定のソート
    return bubble_array

#パーティションで左右に区切る
def partition(array, prime, last):
    low_group  = prime
    for check in range(prime, last):
        if array[check][1]<= array[last][1]:
            array[low_group], array[check] = array[check], array[low_group]
            #値を小さいグループに入れ、グループからはじき出された値は後方のグループの空いた部分に入れる
            low_group += 1
        #値の小さいグループを見つけ出し、最後にパーティションを置く領域を用意する(最後のlow_groupは値の小さいグループには所属しない)
    array[low_group], array[last] = array[last], array[low_group]
    #最後にパーティション値を、小さい値のグループと大きい値のグループにわけるように置く
    partition= low_group
    return partition

#クイックソート
def quick_sort(quick_array,prime,last):
    if prime<last:
        partition_position=partition(quick_array,prime,last)
        #パーティションで左右に区切る
        quick_sort(quick_array,prime,partition_position-1)
        #左側の領域をパーティションを用いたソートする
        quick_sort(quick_array,partition_position+1,last)
        #右側の領域をパーティションを用いたソートする
    return quick_array

lenth = int(input())
card_box=[]

count=0
while count<=lenth-1:
    card=[]
    pattern,number=input().split()
    number=int(number)
    card.append(pattern)
    card.append(number)
    card_box.append(card)
    count+=1

bubble_array=card_box[:]
quick_array= card_box[:]
#別々のソートに分けるため独立した同じ配列を作る
#全要素を取り出す

bubble_array=bubble_sort(bubble_array,lenth)
quick_array=quick_sort(quick_array,0,lenth-1)
#print(*quick_array)

if bubble_array == quick_array:
    print("Stable")
else:
    print("Not stable")
#複数の配列を１つのfor文に同時に回す方法
#https://qiita.com/taku_hito/items/b78b06c42cb0c28af16e

for index in quick_array:
    print(*index)


