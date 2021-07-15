qlist = []

def enq(a):
  qlist.append(a)

def deq():
  b = qlist[0]
  del qlist[0]
  return b

#enqueue test
for i in range(5):
  enq(i)

print(qlist) 

#dequeue test
deq()
print(qlist)
