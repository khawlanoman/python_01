class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name}(Flower):{self.height}cm, {self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age ,trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name}(Tree):{self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {int(self.trunk_diameter * (3.14 / 2))} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season= harvest_season
        self.nutritional_value = nutritional_value

        print(f"{self.name}(Vegetable):{self.height}cm, {self.age} days, summer harvest")
        print(f"{self.name}  is {self.harvest_season} in {self.nutritional_value} ")



print(" === Garden Plant Types ===\n")
Rose = Flower("Rose",25,30,"red")
Rose.bloom()
print("\n")
Oak = Tree("Oak",500,1825,50)
Oak.produce_shade()
print("\n")
Tomato = Vegetable("Tomato",80,90,"rich" ,"vitamin C")
