lenth=int(input())
lenth_in=0
array=[]
prime_array=[]

while lenth_in<=lenth-1:
    input_data=int(input())
    array.append(input_data)
    lenth_in +=1
#配列を1行ずつ入力

for index in array:
    prime_check=2
    #素数の特徴である、１とその数自身以外は割り切れない領域を確保するため
    if index>=2:
    #1は例外のため除外する
        while prime_check<=index:
            if prime_check<index and index % prime_check==0:
                break
            #素数に該当しない数で割り切れた場合、その数は素数ではないのでここで終了する
            if prime_check==index:
                prime_array.append(index)
            #素数に該当しない数で割り切れず最後まで進んだ場合、その数は素数なので素数のリストに追加する
            prime_check+=1
    #2以降の数の処理

#print(prime_array)
print(len(prime_array))