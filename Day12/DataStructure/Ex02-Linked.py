'''
연결 리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것으로
    한 방향으로만 탄생 가능한 구조

node1 = Node(7)
node2 = Node(3)
node3 = Node(9)
node4 = Node(1)
node5 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(id(node1.next))
print(id(node2))
'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init(data):
    global node1
    node1 = Node(data)


def insert(data):
    global node1
    new_node = Node(data)
    current = node1
    while current.next != None:  # 마지막 노드 찾기
        current = current.next

    current.next = new_node


'''

또 다른 방법
def insert(data):
    global node1
    global last_node
    
    new_node = Node(data)
    current = node1
    if current.next is None:
        current.next = new_node    
        last_node = new_node
    else:
        last_node.next = new_node
        last_node = new_node
        
'''


def insertNode(findData, insertData):  # finddata: 9, insertdata: 99
    global node1

    if node1.data == findData: # node1.data : 7 == 9 해당없음
        node = Node(insertData, node1)
        node1 = node
        return

    current = node1             # current.data : 7 / current next: 3
    while current.next != None:
        pre = current
        # print('{}'.format(pre.data)) -> while문 길어지면 print로 찍어보기  # pre.data: 7 | 3 / pre.next: 3 | 9
        current = current.next
                                # current.data:3 | 9 / current.next: 9 | 1
        if current.data == findData:
                                # current.data: 3 | 9 == finddata: 9
            node = Node(insertData, current)  # inserdata: 99, current: 9(주소값)
            pre.next = node                   # pre.data : 3 / pre.next : 9(주소값) --> 99(주소값으로 변경)
            return


def delete(del_data):
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data:
        pre_node.next = next_node.next
        del next_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next


def print_list():  # 연결 리스트의 데이터를 출력한다.
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next
    print()


# 실행코드
init(7)
insert(3)
insert(9)
insert(1)
insert(6)

print_list()
print()

insertNode(9, 99)

print_list()