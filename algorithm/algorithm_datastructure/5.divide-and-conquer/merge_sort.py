array_sum=int(input())
#合計数
array = list(map(int, input().split()))
#使用する数をまとめて配列に入力(但し、必ず昇順で入力する事)
count=0

#統合部
def merge(array, left, mid, right):
    global count
    #カウンターはグローバル変数を使用する
    L = array[left:mid]
    #左側の配列
    R = array[mid:right]
    #右側の配列
    
    for i in range(left,right):
        #左右の配列を比較
        count+=1
        #試行回数をカウント
        if len(L) == 0:
            array[i] = R.pop(0)
        #左側の配列が空の時、右側の配列から数を落とし、配列に組み込む
        #落としたら後方の数が先頭に来る
        elif len(R) == 0:
            array[i] = L.pop(0)
        #右側の配列が空の時、左側の配列から数を落とし、配列に組み込む
        elif L[0] <= R[0]:
            array[i] = L.pop(0)
        #左側の配列の先頭＜右側の配列の時、右側の配列から数を落とし配列に組み込む
        else:
            array[i] = R.pop(0)
        #左側の配列の先頭＞右側の配列の時、左側の配列から数を落とし配列に組み込む
    #統合する配列の範囲内で行う
    

#分割部
def mergesort(array,left,right):
    global count
    #カウンターはグローバル変数を使用する
    if left + 1 < right:
        mid = (left + right)//2
        mergesort(array,left,mid)
        #左半分に分割
        mergesort(array,mid,right)
        #右半分に分割
        merge(array,left,mid,right)
        #配列の結合

mergesort(array,0,array_sum)
print(*array)
print(count)