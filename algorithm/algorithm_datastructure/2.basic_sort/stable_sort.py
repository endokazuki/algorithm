lenth = int(input())
*array, = input().split()
#空白区切りで入れた引数を配列に保存する
#二次元配列を入力
#第一座標：カードの位置、第二座標：0=トランプの絵札,1=トランプの数字
#1次元配列では1枚のトランプのカードとして表示される（二次元配列だと第一座標を示す）
#Excelの資料を参考
#https://qiita.com/muchosucho/items/08ccf26aa77a84678f9a
#print(A[0],A[0][0],A[0][1],A[1],A[1][0],A[1][1])
#H4 H 4 C9 C 9
bubble_array=array[:]
selection_array= array[:]
#別々のソートに分けるため独立した同じ配列を作る
#全要素を取り出す

#range関数
#第１引数：始め、第２引数：終わり、第３引数：ステップ数（方向）
#https://www.javadrive.jp/python/function/index6.html

#バブルソート
for erea in range(lenth):
    for target_point in range(lenth-1, erea, -1):
        #配列の逆から行っている
        if bubble_array[target_point][1] < bubble_array[target_point-1][1]:
            bubble_array[target_point], bubble_array[target_point-1] = bubble_array[target_point-1], bubble_array[target_point]
        #右側のカードの数字が左側のカードの数字より小さい場合、カードの交換を行う
    #print(*array)
#1周すると左端の領域が確定し、その右隣の領域の検証を開始する（これを配列が終わるまで繰り返す）
print(*bubble_array)
print("Stable")
#バブルソートは常に安定のソート

#選択ソート
for erea in range(lenth):
    erea_point = erea
    for target_point in range(erea, lenth):
        if selection_array[target_point][1] < selection_array[erea_point][1]:
            erea_point = target_point
    selection_array[erea], selection_array[erea_point] = selection_array[erea_point], selection_array[erea]
    #選択したカードが左端の領域のカードの数字より小さい場合、カードの交換を行う
    #そうでない場合は自分自身を入れ替える（カードの交換を行わない）
    #print(*selection_array)
#1周すると左端の領域が確定し、その右隣の領域の検証を開始する（これを配列が終わるまで繰り返す）
print(*selection_array)
if bubble_array == selection_array:
    print("Stable")
else:
    print("Not stable")
#選択ソートは安定しないソートなため（数字は正しいが絵札の順番が毎回異なる）、安定するソート（バブルソート）と比較する