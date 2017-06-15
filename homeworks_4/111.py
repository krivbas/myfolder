my_dict = {"first_name":"Nikola",
           "last_name": "Volovets",
           "email":"test@mymail.in.ua",
           "age": 29}

my_dict2 = dict.values(my_dict)

print(my_dict2)

my_dict3 = []

for value in my_dict2:
    if isinstance(value, int):
        if 25 <= value <= 40:
            my_dict3.append(str(value))
    else:
        if len(value) > 5 and value.find("a") >= 0:
            my_dict3.append(value)
print(my_dict3)

if value in my_dict3:
    if value.find("n") >= 0 or value.find("m") >= 0:
        my_dict3.remove(value)
print(my_dict3)

my_dict3.sort(reverse=True)
print(my_dict3)

my_dict4 = ",".join(my_dict3)
print(my_dict4)

my_dict5 = my_dict4.split(",")
print(my_dict5)