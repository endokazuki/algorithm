#バブルソート
#参照：https://codezine.jp/article/detail/12243
lenth=int(input())
#配列数
array = list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方


def bubble_sort(array,lenth):
    i=lenth-1
    i_top=lenth-1
    j=i_top
    #配列の末端
    k=1
    count=0

    while i>=1:
        j=i_top
        while j>=k:
    #確定した配列の直前に到達するまで比較を行う
            if array[j-1]>array[j]:
            #前の配列が後ろの配列よりも値が大きい場合、交換を行う
                array[j-1],array[j]=array[j],array[j-1]
                count+=1
            j-=1
        i-=1
        k+=1
        #確定した配列はこれ以降比較しない
    print(*array)
    print(count)

bubble_sort(array,lenth)

"""
#別解（怪しい）
lenth=int(input())
#配列数
array = list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方
i=0
j=i+1
count=0

while i<=lenth-1:
    while j<=lenth-1:
        if array[j]<=array[i]:
            array[i],array[j]=array[j],array[i]
            count+=1
        j+=1
        
    #print(*array)
    i+=1
    j=i+1

print(*array)
print(count) 

"""