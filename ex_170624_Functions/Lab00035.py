def make_pizza(*topings):
    print(topings)   # tuple
    for topin in topings:
        print(topin)

pramod = make_pizza("tomato")
bhargav =  make_pizza("Olives", "mushroom", "paneer")


# r = max("Amit", 2, 3, 4)  # all datatypes should be same
r = max(1, 2, 3, 4, 4)
print(r)

d = {"name": "Pramod"}
print(d)



def make_pizza(*topins, base):
    print(topins, base)


amit = make_pizza("mushroom", "tomato", base = "thin crust")


