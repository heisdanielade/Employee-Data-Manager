

# # Python List and Variable assignment question.
# x = [1,2,3]
# y = x
# y[0] = 4
# print(x)


# """
#     a.) [1,2,3]
#     b.) [4,2,3]
#     c.) [1,2,3,4]
#     d.) [4,2,3,4]
# """


# y.append(5)
# print(f"y: {y}")
# print(f"x: {x}")


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    

animal = Dog(name="Leosz", breed="German Sheperd", age=7)

print(animal)