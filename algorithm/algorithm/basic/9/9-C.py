a_point,b_point=0,0
game_set=int(input())

for i in range(game_set):
    a_card,b_card=map(str,input().split())
    dictionary=sorted([a_card,b_card])
    #print(a_card,b_card,dictionary)
    battle=[a_card,b_card]
    if a_card==b_card:
        a_point+=1
        b_point+=1
    else:
        if battle==dictionary:
            b_point+=3
        else:
            a_point+=3

print(a_point,b_point)
