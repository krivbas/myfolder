my_dict = {"first_name":"Nikola",
           "last_name": "Volovets",
           "email":"test@mymail.in.ua",
           "age": 29}

print(my_dict.items())

my_dict2 = list(my_dict)

print(my_dict2)

my_dict3 = []

for mylist in my_dict2:
    if isinstance(mylist, str):
        if mylist.find("a") and len(mylist) > 5:
            my_dict3.append(mylist)
        else:
            print("no ok")
    else:
        print("no ok2")
print(my_dict3)