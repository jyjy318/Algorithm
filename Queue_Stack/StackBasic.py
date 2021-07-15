slist = []
def spush(a):
  slist.append(a)
def spop():
  b = slist[-1]
  del slist[-1]
  return b
#테스트 
for i in range(10):
  spush(i)
print(slist)
#pop 테스트
spop()
print(slist)
