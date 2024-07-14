# SET operations

set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set2.issubset(set1))

for i in set1:
    print(i)

print(len(set2))

set1.remove(3)
print(set1)
set1.add(100)
print(set1)

set1.pop()          # Frst element pop out(deleted)
print(set1)