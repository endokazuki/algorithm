# 必要なライブラリのインポート
import queue

no_q = queue.Queue()
data_q=queue.Queue()
# FIFOキューの作成

process,time=map(int,input().split())
process_count=0
timer=0


while process_count !=process:
    no,data=map(str,input().split())
    no_q.put(no)
    data_q.put(int(data))
    #文字型にした数字を数値型に再定義している
    process_count +=1
#キューに初期データを全て入れる

while not no_q.empty():
    out_no=no_q.get()
    out_data=data_q.get()
    #先頭キューの取り出し
    if int(out_data)-time<=0:
        timer+=out_data
        #処理時間を記録する
    #処理が完了するため再度キューには入らない
        print(out_no,timer)
        #完了したプロセス名とそこまでかかった時間を出力する
    else:
        timer+=time
        #最大処理時間を記録する
        out_data=out_data-time
        #残りの処理時間を入れる
        no_q.put(out_no)
        data_q.put(int(out_data))
    #処理が完了しないため再度キューに入る
#キューが空になるまで作業を行う
    