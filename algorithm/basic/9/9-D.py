input_array=list(input())
case=int(input())

for i in range(case):
    action=list(map(str,input().split()))
    start_point=int(action[1])
    end_point=int(action[2])

    #文字の置き換え
    if action[0]=="replace":
        for e,word in enumerate(action[3],start_point):
            input_array[e]=word
        #print(input_array)
            
    #文字の反転
    elif action[0]=="reverse":
        reverse=input_array[start_point:end_point+1]
        #print(reverse)
        reverse.reverse()
        #print(reverse)
        for word in range(len(reverse)):
            input_array[start_point+word]=reverse[word]
        #print(input_array)

    #状態を出力
    elif action[0]=="print":
        print(*input_array[start_point:end_point+1],sep="")
    
    else:
        pass




