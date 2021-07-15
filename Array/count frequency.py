count = 0
for data in dataset:
  for i in range(len(data)):
    if data[i] == "M":
      count +=1
print(count)
