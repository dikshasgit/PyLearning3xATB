# Dictionary to List

my_dict = dict(name="Dave", age=50, address="Pune")
my_list_keys = list(my_dict.keys())
print(my_list_keys)
my_list_values = list(my_dict.values())
print(my_list_values)

for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for i,j in my_dict.items():
    print(i, j, sep=":")

    # Order of dictionary is generally unordered

    my_dict = dict()
    my_dict["b"] = 5
    my_dict["d"] = 4
    my_dict["c"] = 6
    my_dict["a"] = 2

    for i, j in my_dict.items():
        print(i, j)

    from collections import OrderedDict

    od = OrderedDict()
    od["b"] = 50
    od["a"] = 75
    od["d"] = 40
    print(od)