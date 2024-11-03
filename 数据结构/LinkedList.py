class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# 头插法
def create_head(li):
    head = Node(li[0])
    for i in li[1:]:
        node = Node(i)
        node.next = head
        head = node
    return head


# 尾插法
def create_tail(li):
    head = Node(li[0])
    tail = head
    for i in li[1:]:
        node = Node(i)
        tail.next = node
        tail = node
    return head


# 遍历
def print_lk(lk):
    while lk != None:
        print(lk.val)
        lk = lk.next


# 在某元素后添加节点
def add_node(lk, n, v):
    while lk:
        if lk.val == n:
            break
        else:
            lk = lk.next
    node = Node(v)
    node.next = lk.next
    lk.next = node


# 删除某节点
def delete_node(lk, n):
    while lk:
        if lk.next.val == n:
            break
        else:
            lk = lk.next
    p = lk.next
    lk.next = lk.next.nextj
    del(p)


li = [1, 3, 2]
lk = create_tail(li)
add_node(lk, 3, 4)
delete_node(lk, 3)
print_lk(lk)
