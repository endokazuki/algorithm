while True:
#無限ループ
    input_card=input()
    if input_card=="-":
        break
    input_shuffle=int(input())
    for i in range(input_shuffle):
        input_number=int(input())
        input_card=input_card[input_number:]+input_card[:input_number]
        #シャッフルしたカードを上の束に移動させる
    print(input_card)
