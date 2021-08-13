""""
#再帰関数
def sum(n):
    if n <= 0:
        return n
    return n + sum(n-1)
    #10+9+8....+1+0
print(sum(10))
"""

search_sequence_sum=int(input())
#合計数
search_sequence = list(map(int, input().split()))
#使用する数をまとめて配列に入力(但し、必ず昇順で入力する事)
search_sequence_point=0

target_sequence_sum=int(input())
#合計数
target_sequence = list(map(int, input().split()))
#対象の数をまとめて配列に入力
target_sequence_judge=["no"]*target_sequence_sum
#対象の数の結果専用の配列(デフォルトはno(未解決)と置く)
#全パターン検証後は、noは解なしでyesは解ありと判定する

first_array=[]
#insert_array=[]
#non_insert_array=[]


def exhaustive_search(search_sequence_point,result_array):
    non_insert_array=[]
    insert_array=[]
    
    non_insert_array+=result_array
    #上の階層で行った配列を入れる
    #数をいれないケース

    insert_array+=result_array
    #上の階層で行った配列を入れる
    insert_array.append(search_sequence[search_sequence_point])
    #数を入れるケース

    search_sequence_point+=1

    if search_sequence_point==search_sequence_sum:
        target_sequence_point=0
        #print(non_insert_array,insert_array)
        #print(sum(non_insert_array),sum(insert_array))
        #配列内の合計
        while target_sequence_point<=target_sequence_sum-1:
            if sum(non_insert_array)==target_sequence[target_sequence_point] or sum(insert_array)==target_sequence[target_sequence_point]:
                target_sequence_judge[target_sequence_point]="yes"
            target_sequence_point +=1
            #print(target_sequence_judge)
        #使用する数の合計値が対象の数と一致した時、対象の数とリンクした配列の可否を「no→yes」に変更する
    #全ての使用する数の可否を決めた結果を検証対象とする

    if search_sequence_point<=search_sequence_sum-1:

        exhaustive_search(search_sequence_point,non_insert_array)
        #次の階層に数を入れていない配列を使用する

        exhaustive_search(search_sequence_point,insert_array)
        #次の階層に数を入れた配列を使用する
    #配列が残っているとき、次の階層に引き渡す

    
exhaustive_search(search_sequence_point,first_array)
#print(target_sequence_judge)
for judge in target_sequence_judge:
    print(judge)