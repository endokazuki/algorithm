sum_count=int(input())
#入力回数
input_count=0
#配列の先端

class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
   
    def __init__(self):
        self.head = Cell(None)

    def insert(self, value):
        front = self.head
        #front:前方
        rear = front.next
        #後方：rear
        while rear and value > rear.value:
            front = rear
            rear = rear.next
        #挿入先にまだ値が入っていないとき、実行される
        cell = Cell(value)
        cell.next = rear
        front.next = cell
    
    
    
    def delete(self, value):
        front = self.head
        rear = front.next
        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next
        if not rear:
            print("[*] Data not found")
            return
        front.next = rear.next
        rear = None

    def show(self):
        result=[]
        tmp = self.head.next
        while tmp:
            result.append(tmp.value)
            #print(tmp.value)
            tmp = tmp.next
        print(*result)

l = LinkedList()

while input_count<=sum_count-1:
    input_count +=1

    operate,value=map(str,input().split())
    value=int(value)
    if operate=="insert":
        l.insert(value)
    elif operate=="delete":
        l.delete(value)
#配列を1行ずつ入力

l.show()



"""
l = LinkedList()
print('insert 3, 5, 1...')
l.insert(3)
l.insert(5)
l.insert(1)
print('print data')
l.show()
print('delete 3...')
l.delete(3)
print('print data')
l.show()
"""




"""
#イテレータ：リストなどの複数の要素をもったデータ型に対して、順番にデータを取り出す機能を提供する
#self:インスタンス自身

#参照：https://qiita.com/tchnkmr/items/e740173d7400f8672d75

#最大値までのカウントアップのインスタンス
class Seq:
    def __init__(self, max):
    #初期値を決める関数
        self._max = max
        self.pointnumber = 1
         #インスタンス（ここではSeq）のmaxに引数maxを格納する
         #データを取り出す場所を指定する
 
    def __iter__(self):
        return self
        #インスタンスにイテレータの機能を取り付ける
        #正確には__iter__直下にある関数群（__next__）を戻り値としてインスタンス内に格納する事を行う。
    #これがないと、インスタンスはイテレータを持たなくなる
 
    def __next__(self):
        result = self.pointnumber
        if result > self._max: raise StopIteration
        self.pointnumber += 1
        return result
 
seq = Seq(10)
for n in seq:
    print(n, end=" ")

print()

for line in open("C:/Users/endokazuki/Desktop/algorithm/algorithm_datastructure/test.text"):
    print(line)
#行を1行ずつ読み取っている（内部でイテレータが駆動している）


a=[]
a.append([1,2,3,4])
a.append(["a","b","c"])
print(a)
#[[1, 2, 3, 4], ['a', 'b', 'c']]
#配列に配列を格納している
"""