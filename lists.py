# import __hello__

li = [1, 2, 3, 4, 5, 6,"S"]
li.append(7)        #takes 1 value to append
print(li)

li.append((8, 9, 10))
print(li)

li.clear()
print(li)

li = [1, 2, 3, 4, 5, 6]
li2 = li.copy()

li.append(6)
print(li, li2)

print(li.count(6))

print(li.index(4))

li.insert(2, 22)
print(li)

li.pop(1)
print(li)

li.remove(22)
print(li)
