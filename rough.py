lst = [1,2,3]
my_str = "MLOPs Tutorial"
my_int = 155

# print(type(my_str))
# print(type(my_int))
# print(type(lst))

# lst.clear()
# lst.capitalize() # This will raise an AttributeError since lists do not have a capitalize method
# print(lst)
# my_str = my_str.capitalize()
# print(my_str)

# a = 'x'
# b = 'y'

# print(a + b)


# function
# print(len(lst))

# method
from oops_project import chatbook
user1 = chatbook()
# user1.send_msg()
# print(user1.name)
# print(user1.__name)  # This will raise an AttributeError since __name is private
# print(user1._chatbook__name)
# print(user1.get_name())
# print(user1.set_name("New User"))
# print(user1.get_name())

print(user1.id)

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)



















