#5-1
H,W=map(int,input().split())

while H!=0 or W!=0:
    shape=""
    while 0<W:
        shape+="#"
        W-=1
    while 0<H:
        print(shape)
        H-=1
    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する

#5-2
H,W=map(int,input().split())

while H!=0 or W!=0:
    shape=""
    #外側の図形
    shape_index=""
    #内側の図形
    while 0<W:
        shape+="#"
        if shape=="#" or W==1:
            #一番初めと一番最後（図形の外側に相当する部分）に実行
            shape_index+="#"
        else:
            shape_index+="."
        W-=1
    
    print(shape)
    while 1<H-1:
        print(shape_index)
        H-=1
    print(shape)
    #図形の作成


    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する

#5-3
H,W=map(int,input().split())

while H!=0 or W!=0:
    w_sum=W
    switch="off"
    while 0<H:
        W=w_sum
        shape=""
        set_shape=""
        #初期化する値
        
        if switch=="off":
            while 0<W:
                if set_shape=="" or set_shape==".":
                    set_shape="#"
                else:
                    set_shape="."
                shape+=set_shape
                W-=1
            print(shape)
            #奇数部分の図形の描写
            switch="on"
        elif switch=="on":
            while 0<W:
                if set_shape=="" or set_shape=="#":
                    set_shape="."
                else:
                    set_shape="#"
                shape+=set_shape
                W-=1
            print(shape)
            #偶数部分の図形の描写
            switch="off"
        H-=1
    print()
    #最後に空白を作る
    H,W=map(int,input().split())
    #次のフェーズに移行する
