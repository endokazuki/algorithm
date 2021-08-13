

#7-C
class Queue_sum:
    def __init__(self,w,h):
        self.w=w
        self.h=h
    #def __init__(self) -> None:
    # -> は注釈（アノテーション）の事（ここでは初期値を設定していない事を説明している）
    #https://note.nkmk.me/python-function-annotations-typing/
        self.array=None
        self.input_line=None

    def make_queue(self):
        self.array=[[0] * h for i in range(self.w)]
        #print(array)
        #[ 式 for 変数 in オブジェクト ](リスト内包表記法) https://www.nslabs.jp/python-for-keyword.rhtml
        #空の配列リストの作成方法 https://note.nkmk.me/python-list-initialize/
        for i in range(self.w):
            self.input_line = list(map(int,input().split()))
            self.array[i]=self.input_line
        #print(self.array)
        return self.array
    
    def sum_line(self,queue):
        for i in range(self.w):
            sum=0
            for j in range(self.h):
                sum+=queue[i][j]
            queue[i].append(sum)
        return queue
    
    def sum_column(self,queue):
        sum_column=[]
        line_colmn=0
        for i in range(self.h):
            sum=0
            for j in range(self.w):
                sum+=queue[j][i]
            line_colmn+=sum
            sum_column.append(sum)
        sum_column.append(line_colmn)
        return sum_column

a,b,c,d=map(int,input().split())
w,h=map(int,input().split())

queue=Queue_sum(w,h).make_queue()
queue=Queue_sum(w,h).sum_line(queue)
#print(queue)
sum_column=Queue_sum(w,h).sum_column(queue)
queue.append(sum_column)
#print(queue)

print(a,b,c,d)
for i in queue:
    print(*i)
