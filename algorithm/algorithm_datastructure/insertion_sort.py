lenth=int(input())
#配列数
array = list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方

#挿入ソート
#参照：https://www.codereading.com/algo_and_ds/algo/insertion_sort.html

#print(*array)
#配列内を表示
#print(''.join(f'{e:2d}' for e in array))
#配列を取り出し並べて表示

def insertion_sort(array,lenth):
    i=1
    while i <= lenth-1:
        print(*array)
        #配列内を表示
        #*は配列の括弧を削除
        #print(''.join(f'{e:2d}' for e in array))
        #配列を取り出し並べて表示
        v = array[i]
        j = i - 1
        while j >= 0 and array[j] > v:
            array[j+1] = array[j]
            j-=1
    
        array[j+1] = v
        i +=1

    print(*array)
    #最終ソートの結果を出力（while文内ではだせないため）

insertion_sort(array,lenth)

    

