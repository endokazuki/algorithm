search_sequence_sum=int(input())
search_sequence_sum_origin=search_sequence_sum
#合計数は1つの変数に固定で格納
search_sequence = list(map(int, input().split()))
search_sequence_origin=search_sequence
#探索する数をまとめて配列に入力(但し、必ず昇順で入力する事)

search_sequence_mid=int(search_sequence_sum //2)
#配列の両端及び真ん中


"""
今回は計算量時間を少なくするためこれは用いない

search_sequence=(list(set(search_sequence)))
重複した数字を排除
search_sequence_sum=int((len(search_sequence)))
重複のない探索する数の総数を抽出
print(search_sequence_sum)
print(search_sequence)

"""

target_sequence_sum=int(input())
target_sequence = list(map(int, input().split()))
#探索対象の数をまとめて配列に入力


#print(target_sequence)



def binary_search(search_sequence,search_sequence_sum,search_sequence_mid,target_sequence):
    check_target=0
    #該当した数をカウント
    target_sequence_point=0
    #探索対象の数を格納した配列の場所
    while target_sequence_point<=target_sequence_sum-1:
        while search_sequence_sum!=1:
            if target_sequence[target_sequence_point]<search_sequence[search_sequence_mid]:
                search_sequence=search_sequence[0:search_sequence_mid]
                search_sequence_sum=int(len(search_sequence))
                #print("l",search_sequence)
                #分割した後の配列の数
                search_sequence_mid=int(search_sequence_sum //2)
                #分割した先の配列の真ん中を求める
            #左側の配列を探索する

            elif search_sequence[search_sequence_mid]<=target_sequence[target_sequence_point]:
                search_sequence=search_sequence[search_sequence_mid:]
                search_sequence_sum=int(len(search_sequence))
                #分割した後の配列の数
                #print("r",search_sequence)
                search_sequence_mid=int(search_sequence_sum //2)
                #分割した先の配列の真ん中を求める
            #左側の配列を探索する
            
        #配列を分割して１個の配列になるまで分割を行う

        if target_sequence[target_sequence_point]==search_sequence[0]:
            check_target+=1
        else:
            pass
        search_sequence=search_sequence_origin
        search_sequence_sum=search_sequence_sum_origin
        search_sequence_mid=int(search_sequence_sum //2)
        #バラバラになった配列を元に戻す
        target_sequence_point+=1
        #次の数の探索を行う
    print(check_target)

binary_search(search_sequence,search_sequence_sum,search_sequence_mid,target_sequence)