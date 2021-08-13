#各ノード内で最も深い高さを求める
def heights(height,left_degree,right_degree):
    left_height=height
    right_height=height

    if left_degree!=-1:
        left_height+=1
        left_height=heights(left_height,node_list[left_degree][1],node_list[left_degree][2])

    if right_degree!=-1:
        right_height+=1
        right_height=heights(right_height,node_list[right_degree][1],node_list[right_degree][2])
    
    if left_height<=right_height:
        return right_height
    else:
        return left_height


#根を基準に二分木を作成する
def tree(node,parent,sibling,left_degree,right_degree,depth,type):
    global result
    
    #親の子の数
    if left_degree!=-1 and right_degree!=-1:
        degree_nums=2
    elif left_degree!=-1 or right_degree!=-1:
        degree_nums=1
    else:
        degree_nums=0
    
    #各ノードの高さ
    height=heights(0,left_degree,right_degree)
    #print(height)

    #print("node {}: parent = {}, sibling = {}, degree = {}, depth = {},　height = {}, {}".format(node,parent,sibling,degree_nums,depth,height,type))
    result+=[[node,parent,sibling,degree_nums,depth,height,type]]
 
    #次のノードに行くための情報をまとめる
    if left_degree!=-1:
        if node_list[left_degree][1]!=-1 or node_list[left_degree][2]!=-1:
            type="internal node"
            tree(left_degree,node,right_degree,node_list[left_degree][1],node_list[left_degree][2],depth+1,type)
        elif node_list[left_degree][1]==-1 or node_list[left_degree][2]==-1:
            type="leaf"
            tree(left_degree,node,right_degree,-1,-1,depth+1,type)

    if right_degree!=-1:
        if node_list[right_degree][1]!=-1 or node_list[right_degree][2]!=-1:
            type="internal node"
            tree(right_degree,node,left_degree,node_list[right_degree][1],node_list[right_degree][2],depth+1,type)
        elif node_list[right_degree][1]==-1 or node_list[right_degree][2]==-1:
            type="leaf"
            tree(right_degree,node,left_degree,-1,-1,depth+1,type)
    
num=int(input())
node_list=[]

#各ノードのデータ作成
for node in range(num):
    data=[]
    input_data = list(map(int,input().split()))
    #node,degree,c1,c2...(c:child)
    #例）1,2,2,3(1番目のノードで次点が2つある。その子は「2,3」である)
    data+=[input_data[0],input_data[1],input_data[2]]
    #複数のappendを1行にまとめる方法
    #https://qiita.com/tag1216/items/416314cc75a099ad6149
    node_list.append(data)

node_list=sorted(node_list,key=lambda x:(x[0]))
#print(node_list)
#ノードが順番通りではない場合があるので、揃える

#全ノード
all_node=[]
for node in range(num):
    all_node.append(node)
#print(all_node)

#親を持つノードの特定
child_node=[]
for node in node_list:
    #左の子の検証
    if node[1]!=-1:
        child_node.append(node[1])

    #右の子の検証
    if node[2]!=-1:
        child_node.append(node[2])
#print("c",child_node)

#根を持つノードの特定
for node in child_node:
    all_node.remove(node)
root_node=all_node[0]
#print("r",root_node)

left_degree=node_list[root_node][1]
right_degree=node_list[root_node][2]
result=[]
if num==1:
    #ノードが１つしかない場合の処理
    print("node 0: parent = -1, sibling = -1, degree = 0, depth = 0, height = 0, root")
else:
    tree(root_node,-1,-1,left_degree,right_degree,0,"root")
    
    result=sorted(result,key=lambda x:(x[0]))
    
    for node in result:
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"\
            .format(node[0],node[1],node[2],node[3],node[4],node[5],node[6]))
    #pythonの改行方法
    #https://note.nkmk.me/python-long-string/