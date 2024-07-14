# Dictionary -> Key -> Value pairs

my_dict = {"key": "Lock"}
print(my_dict)

my_dict1 = {"name": "Mangesh",
            "age": 45,
            "address": "Pune"}

print(len(my_dict1))
print(len(my_dict1["name"]))
print(my_dict["key"])
print(my_dict1["age"])

# Dictionary -> Key -> Value pairs

my_dict = {"name": "Mangesh",
            "age": 45,
            "address": "Pune"}

dict1 = dict(name="Pramod", age=34, address="Banglore")
print(dict1)

print(dict1.get("age"))
print(dict1["age"])
print(dict1.values())
print(my_dict.keys())