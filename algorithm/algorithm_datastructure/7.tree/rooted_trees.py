def tree(id,p,d,t,degree_numbers,result):
    
    tree_node=id
    tree_parent=p
    tree_depth=d
    tree_type=t
    tree_degree_numbers=degree_numbers
    #print("node {}: parent ={},depth={},{},{}".format(tree_node,tree_parent,tree_depth,tree_type,tree_degree_numbers))
    result+=[[tree_node,tree_parent,tree_depth,tree_type,tree_degree_numbers]]
    
    #次のノードに行くための情報をまとめる
    if tree_degree_numbers!=[]:
        for degree_number in tree_degree_numbers:
            if node_list[degree_number][1]!=0:
                tree_type="internal node"
                tree(degree_number,tree_node,tree_depth+1,tree_type,node_list[int(degree_number)][2],result)
            else:
                tree_type="leaf"
                tree(degree_number,tree_node,tree_depth+1,tree_type,[],result)
    #変数の挿入による出力
    #https://note.nkmk.me/python-print-basic/

num=int(input())
node_list=[]

#各ノードのデータ作成
for node in range(num):
    data=[]
    degree_numbers=[]
    input_data = list(map(int,input().split()))
    #node,degree,c1,c2...(c:child)
    #例）1,2,2,3(1番目のノードで次点が2つある。その子は「2,3」である)
    if input_data[1]!=0:
        degree_numbers.append(input_data[2:])
    #字数が存在する場合の処理
    data+=[input_data[0],input_data[1],*degree_numbers]
    #複数のappendを1行にまとめる方法
    #https://qiita.com/tag1216/items/416314cc75a099ad6149
    node_list.append(data)
#print(node_list)
node_list=sorted(node_list,key=lambda x:(x[0]))
#ノードが順番通りではない場合があるので、揃える

#全ノード
all_node=[]
for node in range(num):
    all_node.append(node)
#print(all_node)
#親を持つノードの特定
child_node=[]
for node in node_list:
    if len(node)==3:
        child_node+=node[2]
    else:
        pass
#print("c",child_node)
#根を持つノードの特定
for node in child_node:
    all_node.remove(node)
root_node=all_node
#print("r",root_node[0])

result=[]
if num==1:
    #ノードが１つしかない場合の処理
    print("node 0: parent = -1, depth = 0, root, []")
else:
    tree(root_node[0],-1,0,"root",node_list[root_node[0]][2],result)
#print(result)
    result=sorted(result,key=lambda x:(x[0]))
    #print(sorted_data)
    for node in result:
        tree_node=node[0]
        tree_parent=node[1]
        tree_depth=node[2]
        tree_type=node[3]
        tree_degree_numbers=node[4]
        print("node {}: parent = {}, depth = {}, {}, {}".format(tree_node,tree_parent,tree_depth,tree_type,tree_degree_numbers))
    #print(node)