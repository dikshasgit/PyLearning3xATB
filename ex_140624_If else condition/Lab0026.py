 #For loop
for counter in range(0, 100):  # 0 -> 99
    print(counter)

for counter in range(0, 100, 2):  # Even numbers
    print(counter)

for counter in range(1, 100, 2):  # Odd numbers
    print(counter)

##  -0,0 +1,16
# for loop
for counter in range(0, 100):  # Even numbers
    print(counter)
    if counter == 5:
        break

print("Outside of the program")

# # Output:
# 0
# 1
# 2
# 3
# 4
# 5
# Outside of the program

