# -0,0 +1,6
# range - Can be negative
# for counter in range(10, 1, -1):
#    print(counter)

for counter in reversed(range(0, 10)):
    print(counter)

# Break - based on the condition out of the loop

# Pass - pass do nothing -> skip

for i in range(10):  # default from 0
    if i == 5:
        pass
    else:
        print(i)


# -0
# 0 + 1, 5
for i in range(1, 10):
    if i % 3 == 0:
        print(i)
    else:
        print(i * 2)
