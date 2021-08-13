lenth = int(input())
array = list(map(int, input().split()))
#パーティションで左右に区切る
def partition(array, prime, last):
    low_group  = prime
    for check in range(prime, last):
        if array[check]<= array[last]:
            array[low_group], array[check] = array[check], array[low_group]
            #値を小さいグループに入れ、グループからはじき出された値は後方のグループの空いた部分に入れる
            low_group += 1
        #値の小さいグループを見つけ出し、最後にパーティションを置く領域を用意する(最後のlow_groupは値の小さいグループには所属しない)
    array[low_group], array[last] = array[last], array[low_group]
    #最後にパーティション値を、小さい値のグループと大きい値のグループにわけるように置く
    array[low_group]="[{}]".format(array[low_group])
    #値の前後に[]を挿入
    print(*array)

partition(array,0,lenth-1)