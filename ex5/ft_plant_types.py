class Plant:
    """this class is the parent """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """this class is inherity from class plant
        to manager the type flower from plants"""
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """this methode is show the details from type Flower"""
        print(f"{self.name}(Flower):{self.height}cm,"
              f"{self.age} days, {self.color} color"
              )
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """this class is inherity  from  class
      plant to manager the type tree from plants"""
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """this methode is to calculate the trunk
          and show the details form type Tree"""
        print(f"{self.name}(Tree):{self.height}cm,"
              f"{self.age} days, {self.trunk_diameter}cm diameter"
              )
        print(f"{self.name} provides "
              f"{int(self.trunk_diameter * (3.14 / 2))}"
              f" square meters of shade"
              )


class Vegetable(Plant):
    """this class is inherity  from  class plant
      to manager the type Vegetable from plants"""
    def __init__(self, name, height,
                 age, harvest_season, nutritional_value
                 ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

        print(f"{self.name}(Vegetable):{self.height}cm,"
              f"{self.age} days, summer harvest"
              )
        print(f"{self.name}  is {self.harvest_season}"
              f"in {self.nutritional_value} "
              )


print(" === Garden Plant Types ===\n")
Rose = Flower("Rose", 25, 30, "red")
Rose.bloom()
print("\n")
Oak = Tree("Oak", 500, 1825, 50)
Oak.produce_shade()
print("\n")
Tomato = Vegetable("Tomato", 80, 90, "rich", "vitamin C")
