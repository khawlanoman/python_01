class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.count_grow = 0
        self.type = "regular"
        self.prize = 0 

    def grow(self):
        self.height += 1
        self.count_grow += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def bloom(self):
        print(f"{self.name} ({self.color}) is blooming")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize
        self.type = "prize"

    def display_prize(self):
        print(f"{self.name} prize points: {self.prize}")


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants += [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        total = 0
        for plant in self.plants:
            plant.grow()
            total += plant.count_grow
        return total

    def count_types(self):
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
        score = 0
        for plant in self.plants:
            score += plant.height
            score += plant.prize
        return score


class GardenManager:
    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden):
        self.gardens[garden.name] = garden

    def report(self):
        total_gardens = 0
        total_plants = 0

        for name in self.gardens:
            garden = self.gardens[name]
            total_gardens += 1
            for plant in garden.plants:
                total_plants += 1

        print(f"Total gardens: {total_gardens} Total plants: {total_plants}")



print("=== Garden Management System Demo ===")
manager = GardenManager()

alice = Garden("Alice")
bob = Garden("Bob")

alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 26, "red"))
alice.add_plant(PrizeFlower("Sunflower", 51, "yellow", 10))

bob.add_plant(Plant("Pine", 80))
bob.add_plant(FloweringPlant("Lavender", 11, "purple"))

manager.add_garden(alice)
manager.add_garden(bob)

manager.report()

print("Alice score:", alice.get_score())
print("Bob score:", bob.get_score())
