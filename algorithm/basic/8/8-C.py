import string
import sys

sentence=sys.stdin.read()
#標準入力の方法
#https://algorithm.joho.info/programming/python-sys-stdin-readline/
#print(sentence)

a=string.ascii_uppercase
b=string.ascii_lowercase
alphabet_sum=[0]*26


for i in range(len(sentence)):
    for j in range(26):
        if sentence[i]==a[j] or sentence[i]==b[j]:
             alphabet_sum[j]+=1


for i in range(len(b)):
    print("{} : {}".format(b[i],alphabet_sum[i]))