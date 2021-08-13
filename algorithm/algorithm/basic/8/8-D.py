#8-D
array=str(input())

#tail=int(len(array))-1
#print(head,tail)
#print(array[head],array[tail])
search=str(input())

head=int(-len(array))
tail=len(search)
#print(array[head:len(search)])
#print(search[0:len(search)])
search_count=0
find="No"

while search_count<=len(array) and find=="No":
    loop=array[head:]+array[:tail]
    #環状に繋がった文字列

    if array[head:tail]==search[0:len(search)]:
        find="Yes"
    elif loop==search[0:len(search)]:
        find="Yes"
    print(array[head:tail],":",array[head:],array[:tail],":",loop,":",head,tail)
    head+=1
    tail+=1
    if len(array)<tail:
        tail=1
    search_count+=1
print(find)