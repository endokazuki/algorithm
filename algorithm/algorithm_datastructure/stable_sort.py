lenth=int(input())
#配列数
array= list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方

class sort:
    #バブルソート
    #参照：https://codezine.jp/article/detail/12243
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

    def selection_sort(array,lenth):
        i=0
        j=i
        count=0

        while i<=lenth-1:
            minj=i
            while j<=lenth-1:
                if array[j]<array[minj]:
                    minj=j
                j+=1
            array[i],array[minj]=array[minj],array[i]
            #最小値との入れ替え（ない場合は自分自身を入れ替える）
            if array[i]!=array[minj]:
                count+=1
            else:
                pass
            #入れ替えが行われた時カウントを行う
        
            i+=1
            j=i
            #初期化
    
        print(*array)
        print(count)

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

print(array,lenth)
sort.bubble_sort(array,lenth)
sort.selection_sort(array,lenth)
sort.insertion_sort(array,lenth)
print(array,lenth)
