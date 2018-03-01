
class retaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def open_rastaurant(self):
        print(self.restaurant_name + "is open.")
    def set_number_served(self):
        print(self.number_served)
    def increment_number_served(self):
        print(self.number_served)

res_name = retaurant("PC", "5 stars")
#print(res_name.restaurant_name.title(), res_name.cuisine_type)

res_name.number_served = 10
res_name.set_number_served()





