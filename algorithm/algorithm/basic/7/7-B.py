#7-B
import itertools
#https://qiita.com/Mohrey/items/b0afc8edc5fed742b68a
#【Python】リスト内の要素の全ての組み合わせを出力

class Three_pair:
    def __init__(self):
        self.num_array=[]
        self.match_count=0

    def action(self,n,x):
        #1からnまでの数の配列作成
        for num in range(n):
            self.num_array.append(num+1)
        #1からnまでの数から３つの数を選択した時の結果の検証
        for pair in itertools.combinations(self.num_array, 3):
            #print(pair)
            sum=pair[0]+pair[1]+pair[2]
            if sum==x:
                self.match_count+=1
            else:
                pass
        print(self.match_count)


n,x=map(int,input().split())

while n!=0 or x!=0:
    three_pair=Three_pair().action(n,x)
    n,x=map(int,input().split())
