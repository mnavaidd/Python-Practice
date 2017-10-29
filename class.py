class flower():
    def __init__(self, name):
        self.name = name

    def color(self):
        print(self.name + " color is white")
    def kingdom(self):
        print(self.name + " kingdom is plantae.")
    def order(self):
        print(self.name + " order is Lamiales.")
    def family(self):
        print(self.name + " family is Oleaceae.")
    def tribe(self):
        print(self.name + " tribe is Jasmineae.")
    def genus(self):
        print(self.name + " genus is Jasminum L.")

flower_characteristic = flower("Jasimine's")
flower_characteristic.color()
flower_characteristic.kingdom()
flower_characteristic.order()
flower_characteristic.family()
flower_characteristic.tribe()
flower_characteristic.genus()




