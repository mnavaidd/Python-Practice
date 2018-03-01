class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + "roll over.")


my_dog = Dog("willie", 6)
print("My dog name is " + my_dog.name + " and dog is " + str(my_dog.age) + " years old")

class retaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def open_rastaurant(self):
        print(self.restaurant_name + "is open.")

res_name = retaurant("PC", "5 stars")
