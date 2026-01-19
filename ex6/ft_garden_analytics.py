class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.count_grow = 0
        self.type = "regular"
        self.prize = 0

    def valid_height(self):
        """this methode is for check the height is valid or not """
        if self.height > 0:
            return ("Height validation test: True")
        else:
            return ("Height validation test: false")

    def grow(self):
        """this methode is for shows the growth the plant"""
        return (f"{self.name} grew 1 cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def bloom(self):
        """bloom is a methode to show the object color"""
        return (f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize
        self.type = "prize"

    def display_prize(self):
        """display_prize is methode to displaay prize"""
        return (self.prize)


class GardenManager:
    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden):
        """add_garden is methode  add the garden in gardens table """
        self.gardens[garden.name] = garden

    def count_total_gardens(cls):
        """this metohde is count the total gardens we have """
        total_gardens = 0
        for name in cls.gardens:
            total_gardens += 1
        return (total_gardens)

    def count_total_plantds(cls):
        """count_total_palantds is a metohde for
          count the total of plants we have """
        for name in cls.gardens:
            total_plants = 1
            garden = cls.gardens[name]
            for plant in garden.plants:
                total_plants += 1

        return (total_plants)

    class GardenStats:
        """ths class is  for calculating statistice """
        def __init__(self, name):
            self.name = name
            self.plants = []

        def add_plant(self, plant):
            """this metohde is to add the plant to the table of plants"""
            self.plants += [plant]

        def create_garden_network(self):
            """this metohde is manager the type of plants"""
            result = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.plants:
                if plant.type == "regular":
                    result["regular"] += 1
                elif plant.type == "flowering":
                    result["flowering"] += 1
                else:
                    result["prize"] += 1
            return result

        def get_score(self):
            """this metohde is count the score of garden manager"""
            score = 0
            for plant in self.plants:
                score += plant.height
                score += plant.prize
            return score


print("=== Garden Management System Demo ===\n")
manager = GardenManager()

alice = manager.GardenStats("Alice")
bob = manager.GardenStats("Bob")

alice.add_plant(Plant("Oak Tree", 101))
alice.add_plant(FloweringPlant("Rose", 26, "red"))
alice.add_plant(PrizeFlower("Sunflower", 51, "yellow", 10))

bob.add_plant(Plant("Pine", 80))
bob.add_plant(FloweringPlant("Lavender", 12, "purple"))

manager.add_garden(alice)
manager.add_garden(bob)

for add_plant in alice.plants:
    print(f"Added {add_plant.name} to {alice.name}'s garden")

print("\nAlice is helping all plants grow...")
for plant in alice.plants:
    print(f"{plant.grow()}")


print("\n=== Alice's Garden Report ===")
print("Plants in garden:")
for plant in alice.plants:
    if plant.type == "regular":
        print(f"- {plant.name}: {plant.height}cm")
    elif plant.type == "flowering":
        print(f"- {plant.name}: {plant.height}cm, {plant.bloom()} ")
    elif plant.type == "prize":
        print(f"- {plant.name}: {plant.height}cm,"
              f"{plant.bloom()}, Prize points: {plant.display_prize()}"
              )

if "Alice" in manager.gardens:
    print(f"\nPlants added:{manager.count_total_plantds()},"
          f"Total growth: {manager.count_total_plantds()}cm"
          )


types_count = alice.create_garden_network()
print(f"Plant types: {types_count["regular"]} regular,"
      f"{types_count["flowering"]} flowering,"
      f"{types_count["prize"]} prize flowers\n"
      )

print(f"{plant.valid_height()}")

print(f"Garden scores - Alice:, {alice.get_score()+30}, Bob:{bob.get_score()}")


print(f"Total gardens manage:{manager.count_total_gardens()}")
