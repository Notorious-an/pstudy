'''
연결리스트

    저장된 각 데이터가 데이터+다음 데이터의 포인터로 이루어진 것으로__
    한방향으로만 탐색 가능한 구조

node1 = Node(7)
node2 = Node(3)
node3 = Node(9)
node4 = Node(1)
node5 = Node(1)


node1.next = node2
node2.next = node3
node2.next = node4
node4.next = node5

print(id(node1.next))
print(id(node2))
'''

# 노드 정의
class Node :
    def __init__(self, data, next=None): # data만 입력시 next 초기값은 None이다.
        self.data = data
        self.next = next #다음 데이터 주소 초기값 = None

# Node 생성해보기 (data = 1), 헤드값
node1 = Node(1)

# Node 값과 포인터 출력하기
print(node1.data, node1.next) # 헤드 값이니까 data = 1, next(주소값) 값은 없음

# Node2 생성해보기
node2 = Node(3)

# 연결하기
node1.next = node2

# node1을 통해 연결한 결과 확인(밑 2줄은 동일한 결과를 가리킨다)
print(node1.next.data)
print(node2.data)


# 유툽보고 다시 실행해보기

head_node = Node(1)
head_node.next = Node(2)
head_node.next.next = Node(3)
head_node.next.next.next = Node(4)

def printNodes(node:Node):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.data, end = ' ')
        crnt_node = crnt_node.next




class SLinkedlist:
    def __init__(self):
        self.head = None

    def addAtHead(self, data):   # 헤드 만들기
        node = Node(data) # 새로운 노드 생성
        node.next = self.head # none 값을 next 값으로 지정
        self.head = node  # 현재 node를 새로운 head로 정의  (head를 여러개 추가할 수 있기 떄문)

    def addBack(self, data): # 노드 가하기
        node = Node(data) # 새로운 노드 만들기
        crnt_node = self.head # head로 부터 시작해서
        while crnt_node.next : #next값이 있을떄까지 crnt 노드 값을 바꿔주면서 뒤로 전달
            crnt_node = crnt_node.next
        crnt_node.next = node # 마지막 주소값이 가리키는 것을 현재 node 값으로 지정

# find 함수 만들기
    def findNode(self, data):
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.data == data:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node is not found')
# 중간에 삽입하는 함수 만들기
    def addAfter(self, node, data): # 여기서 node란 그 node 뒤에 생성한다는 뜻
        new_node = Node(data) # 삽입할 새로운 node 만들기
        new_node.next = node.next # 삽입할 node의 next 값에 바로 앞에 있는 node next값 넣어줌
        node.next = new_node # 앞에 있는 node 값에 new node 값 넣어줌

# 중간에 node 삭제하는 함수 만들기
    def deleteAfter(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

print("SLinkedlist 실행해보기")

slist = SLinkedlist()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(4)

node2 = slist.findNode(2) # 값1 을 가지고 있는 node1 return 받기
slist.addAfter(node2,3)
slist.deleteAfter(node2)
printNodes(slist.head)



# 중간에 node 삽입 해보기

