search_sequence_sum=int(input())
search_sequence = list(map(int, input().split()))
#探索する数をまとめて配列に入力
search_sequence=(list(set(search_sequence)))
#重複した数字を排除
search_sequence_sum=int((len(search_sequence)))
#重複のない探索する数の総数を抽出
#print(search_sequence_sum)
#print(search_sequence)

target_sequence_sum=int(input())
target_sequence = list(map(int, input().split()))
#探索対象の数をまとめて配列に入力

#print(target_sequence)

def liner_search(search_sequence_sum,search_sequence,target_sequence_sum,target_sequence):
    check_target=0
    #該当した数をカウント
    search_sequence_point=0
    #探索する数を格納した配列の場所
    target_sequence_point=0
    #探索対象の数を格納した配列の場所
    while search_sequence_point<=search_sequence_sum-1:
        while target_sequence_point<=target_sequence_sum-1:
            if search_sequence[search_sequence_point]==target_sequence[target_sequence_point]:
            #探索する数字が探索対象と合致した場合、カウントを行う
                check_target+=1
                break
                #合致した時点で、それ以降に同じ数は存在しないためこのタームの探索は終了する（内側のwhile文の終了）
            target_sequence_point+=1
        target_sequence_point=0
        #（次の探索を行う時、）探索対象の配列位置を始めに戻す
        search_sequence_point+=1
    print(check_target)
    #合致した数の総数を出力

liner_search(search_sequence_sum,search_sequence,target_sequence_sum,target_sequence)