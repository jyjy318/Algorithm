class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class ManageNode:
  def __init__(self, data):
    self.head = Node(data)

  def add(self, data):
    if self.head == '':
      self.head  = Node(data)
    else:
      node = self.head
      while node.next != None:
        node = node.next
      node.next = Node(data)
  
  def showdata(self):
    node = self.head
    while self.head != None:
      print(self.data)
      node = node.next
  
  def delect(self, data):
    #head가 없는 경우
    if self.head == ' ':
      print("해당 값을 가진 것이 없습니다.")
    #head를 삭제해야 하는 경우
    if self.head.data == data:
      a = self.head
      self.head = self.head.next
      del a
    else:
      node = self.head
      while node.next != None:
        if node.next.data == data:
          b = node.next
          node.next = node.next.next
          del b
        else:
          node = node.next
  # 특정값 노드 찾기
  def searchdata(self, data):
    node = head.self
    while node.next != None:
      if node.data == data:
        return node
      else:
        node = node.next
