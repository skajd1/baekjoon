n = int(input())
tree = {chr(i+65):[] for i in range(n)}
for p,l,r in [list(input().strip().split()) for _ in range(n)]:
    tree[p].append(l)
    tree[p].append(r)

preorder = []
inorder = []
postorder = []
def trav_pre(node):
    if node == '.' :
        return
    preorder.append(node)
    trav_pre(tree[node][0])
    trav_pre(tree[node][1])
def trav_in(node):
    if node == '.' :
        return
    trav_in(tree[node][0])
    inorder.append(node)
    trav_in(tree[node][1])
def trav_post(node):
    if node == '.' :
        return
    trav_post(tree[node][0])
    trav_post(tree[node][1])
    postorder.append(node)

trav_pre('A')
trav_in('A')
trav_post('A')
print(*preorder,sep='')
print(*inorder,sep='')
print(*postorder,sep='')