import queue
data = queue.PriorityQueue()
#앞부분이 우선순위를 나타내는 숫자
data.put((7, "soccer"))
data.put((3, "baseball"))
data.put((5, "swim"))
data.get()   # 우선순위가 가장 높은 (3,'baseball')을 얻을 수 있음
