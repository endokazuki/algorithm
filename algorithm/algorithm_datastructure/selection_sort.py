#選択ソート
lenth=int(input())
#配列数
array = list(map(int, input().split()))
#分割した複数の変数をリスト（配列）にして格納
#配列の作り方

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

selection_sort(array,lenth)