# Tuples

t = tuple()
print(t)

t1 = tuple(["Mangesh", "Pramod", "Mani"])
print(t1)

del t1              # not working?
print(t1)



# Tuple addition

hero1 = tuple("Mangesh", "Dave")
hero2 = tuple("Rani", "Mukharjee")
hero3 = tuple(hero1 + hero2)
# new_tuple = (hero3)              # Not working
print(hero3)