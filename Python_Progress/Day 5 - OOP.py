# class Sample(): # captialize name from classes
#   def __init__(self)
# called upon every time we create an instance of the class
# always start with self keyword to connect the method to instance of the class (allows us to refer it to itself)

# my_sample = Sample()
# print(type(my_sample)) # we created a sample type

# __main__ means it connects to the class


# class Dog():

#   # class object attribute (goes before the constructor function)
#   # same for any instance of a class

#   species = "mammal"

#   def __init__(self, breed, name, spots): #constructor function for a class
#     self.breed = breed # attribute are characteristics of the object
# # we taking in the argument
# # assign it using the self.attribute_name

#     self.name = name
#     self.spots = spots

#   #operations/actions (methods)
#   def bark(self, number):
#     print("WOOF! My name is {} and the number is {}".format(self.name, number))
# # must reference the name of the instance
# new_dog = Dog(breed="shiba inu", name="Money", spots=False)

# print(new_dog.breed)
# print(new_dog.name)
# print(new_dog.spots)
# print(new_dog.species)

# #  what is the difference between functions and methods?
# # methods are functions in a class that will work with the object
# new_dog.bark(number= 4)

# class Circle():
#   # class object attribute
#   pi = 3.14

#   # constructor function
#   def __init__(self, radius=1):
#     self.radius = radius
#     self.area = radius ** 2 * self.pi # or Circle.pi

#   # method
#   def get_circumference(self):
#     return self.radius * self.pi * 2 # or Circle.pi for readability

# my_circle = Circle(5)
# print(my_circle.get_circumference())

# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)


# base class

# class Animal():

#   def __init__(self):
#     print("Animal Created")

#   def who_am_i(self):
#     print("I am an animal")

#   def eat(self):
#     print("I am eating")

# new_animal = Animal()
# new_animal.who_am_i()
# new_animal.eat()

# class Dog(Animal):

#   def __init__(self):
#     Animal.__init__(self) # called the Animal class in the constructor function
#     print("Dog Created")

#   # to rewrite methods in this class use the same name of the method
#   def who_am_i(self):
#     print("I am a dog")

#   # can add on methods too
#   def bark(self):
#     print("WOOF!")

# my_dog = Dog()

# #output
# # Animal Created
# # Dog Created

# my_dog.who_am_i()

# # the dog class can now use methods from the Animal class through inheritance

# my_dog.bark()

# class Book():
#   def __init__(self, title, author, pages):
#     self.title = title
#     self.author = author
#     self.pages = pages

#   def __str__(self):
#     return (f"My book is called {self.title} and the author is {self.author}")

#   def __len__(self):
#     return self.pages

#   def __del__(self):
#     print("A book object has been deleted")

# # need to return and not print for the special dunder method

# my_book = Book("Python", "Monty", 300)

# print(my_book) # uses the special str method in the class I created
# print(str(my_book))
# print(len(my_book))

# # to delete the book from memory (need to use del keyword)
# # want to outout a statement saying we deleted a book (use __del__)

# del(my_book)

# print(my_book) # returns book not defined

# class Line():

#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (abs(x1 - x2)**2 + abs(y1 -y2)**2)**0.5

#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (y1 -y2)/(x1 - x2)

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)

# print(li.distance())
# print(li.slope())

# to get the distance I need to find the difference of the x coordinates and the difference of the y coordinates and then use the pythagorean theorem to find the distance between the 2 points
# I need to use tuple unpacking to get the x coordinates and y cooridinates isolated

#to get the slope of the line segement I need to use the equation y = mx, to get the slope m =y/x

# class Cylinder():

#     pi = 3.14

#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return self.pi * self.radius ** 2 * self.height

#     def surface_area(self):
#         return 2 * self.pi * self.radius ** 2 + 2 * self.radius *           self.pi * self.height


# c = Cylinder(2,3)

# print(c.volume())
# print(c.surface_area())

# volume = pi * radius * radius * height
# surface_area = 2 * pi * radius ** 2 + 2 * radius * pi * height

#OOP challenge

# class Account():

#   def __init__(self, owner, balance=0):
#     self.owner = owner
#     self.balance = balance

#   def __str__(self):
#     return (f"Account Owner: {self.owner}\nAccount Balance:  ${self.balance}")

#   def deposit(self, amount):
#     self.balance = self.balance + amount
#     print("Deposit Accepted")

#   def withdraw(self, amount):
#     if amount > self.balance:
#       print("Insufficient Funds!")
#     else:
#       self.balance = self.balance - amount
#       print("Withdraw Accepted")

# my_account = Account("Philip", 100)

# print(my_account.owner)
# print(my_account.balance)
# print(my_account)

# my_account.deposit(50)
# print(my_account.balance)
# my_account.withdraw(75)
# print(my_account.balance)
# my_account.withdraw(500)
# print(my_account.balance)