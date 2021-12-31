def num(list):
  i= 0
  while i < len(list):
    item = list[i]
    if item > 20:
      list.remove(item)
    else:
      i+= 1
  return list

a= [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = num(a)

print ("Initial list", a)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)