
array =[]
lenth=int(input())
#配列数の入力
lenth_in=0
#配列の先端

while lenth_in<=lenth-1:
    input_data=int(input())
    array.append(input_data)
    lenth_in +=1
#配列を1行ずつ入力

def insertion_sort(array,lenth,interval,result):
    i=interval
    while i <= lenth-1:
        #print(*array)
        #配列内を表示
        v = array[i]
        j = i - interval
        while j >= 0 and array[j] > v:
            array[j+interval] = array[j]
            j-=interval
            result+=1
        array[j+interval] = v
        i +=1
    return result
    #print(*array)
    #各間隔間の最終ソートの結果を出力（while文内ではだせないため）
#各間隔間の挿入ソート

def shell_sort(array,lenth):
    result=0
    interval=0
    interval_list=[]
    sequence=1

    while sequence<=lenth:
        interval_list.append(sequence)
        sequence=3*sequence+1
    interval_list.append(sequence)
    #間隔値はlenthより大きいものを１つ作成する（while文内では作成できないため）
    #数列a(n+1)=3*a(n)+1
    #print(interval_list)


    list_no=0
    while interval<=lenth:
        interval=interval_list[list_no]
        if interval<=lenth:
            list_no+=1
        else:
            pass
        #interval増大後にlist_noの数がずれないための措置
    #配列間の間隔
    print(list_no)
    #使用した間隔の総数

    output_interval=[]
    selected_list_no=list_no-1
    while selected_list_no>=0:
        output_interval.append(interval_list[selected_list_no])
        selected_list_no-=1
    print(*output_interval)
    #使用した間隔を全て表示

    sum_count_result=0
    while 0<=list_no:
        count_result=insertion_sort(array,lenth,interval_list[list_no],result)
        #試行回数は出力する必要があるため、戻り値を変数に格納
        #ちなみに、1番はじめのソートは間隔値が数の個数より多いためソートは0回になる
        sum_count_result+=count_result
        list_no-=1
    print(sum_count_result)
    #シェルソートを実行する
    #この時、試行回数も記録する

    
    for array_result in array:
        print(array_result)
    #ソートの結果を1行ずつ出力

shell_sort(array,lenth)

