word=str(input()).upper()
word_count=0
sentence=list(map(str,input().split()))

while sentence[0]!="END_OF_TEXT":
    for i in range(len(sentence)):
        sentence[i]=sentence[i].upper()
        if sentence[i]==word:
            word_count+=1

    sentence=list(map(str,input().split()))

print(word_count)
