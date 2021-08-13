""""
#再帰関数
def sum(n):
    if n <= 0:
        return n
    return n + sum(n-1)
    #10+9+8....+1+0
print(sum(10))
"""

from itertools import product
#list(product([False, True], repeat=3))#2^3通り
#[(False, False, False), (False, False, True), (False, True, False), (False, True, True),
#(True, False, False), (True, False, True), (True, True, False), (True, True, True)]

search_sequence_sum=int(input())
#合計数
search_sequence = list(map(int, input().split()))
#探索する数をまとめて配列に入力(但し、必ず昇順で入力する事)
target_sequence_sum=int(input())
#合計数
target_sequence = list(map(int, input().split()))
#対象の数をまとめて配列に入力
target_sequence_judge=["no"]*target_sequence_sum
#対象の数の結果専用の配列(デフォルトはno(未解決)と置く)
#全パターン検証後は、noは解なしでyesは解ありと判定する

selection_list=list(product(['False','True'], repeat=search_sequence_sum))
#print(selection_list[31])
#print(selection_list[1][4])
#数字を5つ選んだ場合
#section_list[0][0]...[4][4](25パターン)


def result(search_sequence_sum,search_sequence,target_sequence_sum,target_sequence,target_sequence_judge,selection_list):
    pattern=0
    select=0
    select_sequence_sum=0
    target_sequence_point=0
    while pattern<=2**search_sequence_sum-1:
        #組み合わせは2**（配列数）パターン存在する
        while select<=search_sequence_sum-1:
            judge=selection_list[pattern][select]
            if judge=='True':
                select_sequence_sum+=search_sequence[select]
            else:
                pass
            select+=1
        #各パターン内でTrueであった場合、Trueに属する数を合算する

        while target_sequence_point<=target_sequence_sum-1:
            if target_sequence[target_sequence_point]==select_sequence_sum:
                target_sequence_judge[target_sequence_point]="yes"
            else:
                pass
            target_sequence_point+=1
        #各パターンの合算結果と対象の数が同値であるものをyes(解あり)と判定する

        target_sequence_point=0
        select_sequence_sum=0
        select=0
        #初期化
        pattern+=1

    #print(target_sequence_judge)
    for output_judge in target_sequence_judge:
        print(output_judge)
    #結果を出力

result(search_sequence_sum,search_sequence,target_sequence_sum,target_sequence,target_sequence_judge,selection_list)
    