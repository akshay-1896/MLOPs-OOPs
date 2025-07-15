# initiate a class
class employee:
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        # print("Started initialising attributes!!")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("Attributes are initialized")
        
    def travel(self, destination):
        print("This travel method was called manually")
        # print(f"Employee with ID {self.id} is traveling to {destination}.")


# create an object/instance of the class
sam = employee()

# calling attributes
# print(sam.id)
# print(sam.designation)
# print(sam.salary)

# calling a method
# sam.travel("Kerala")

print(type(sam))