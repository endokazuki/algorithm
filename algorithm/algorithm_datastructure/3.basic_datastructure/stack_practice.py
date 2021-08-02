s = list(input().split())
#入力したデータを配列として保存
stack = []
#スタック（最後に入ったデータが最初に取り出される。箱のようなイメージ）

for i in range(len(s)):
    #配列を前から順番にスタックに入れる
    if s[i] == '+':
        stack.append(stack.pop() + stack.pop())
        #1つ前にあったスタックと2つ前にあったスタックを取り出し足し算を行い、その結果をスタックに再度入れ込む
    elif s[i] == '-':
        stack.append(-(stack.pop() - stack.pop()))
        #1つ前にあったスタックと2つ前にあったスタックを取り出し引き算を行い、その結果をスタックに再度入れ込む
        #-(stack.pop() - stack.pop()):(2つ前にあったスタック)-(1つ前にあったスタック)
    elif s[i] == '*':
        stack.append(stack.pop() * stack.pop())
        #1つ前にあったスタックと2つ前にあったスタックを取り出し掛け算を行い、その結果をスタックに再度入れ込む
    elif s[i] == '/':
        stack.append(round(1/stack.pop() * stack.pop(),1))
        #1つ前にあったスタックと2つ前にあったスタックを取り出し割り算を行い、その結果をスタックに再度入れ込む
        #少数点以下はroundで丸める(今回は小数点第1位まで表示)
        #参照：https://www.headboost.jp/python-how-to-handle-digits/#11
    else:
        stack.append(int(s[i]))
        #配列内の要素が数字だった場合スタック内に保存する

print(*stack)
print(stack[-1])
#スタックの結果表示