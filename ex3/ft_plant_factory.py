class Plant:
    """this class  plant to create the  plant
        objects and count the  number of objects """
    count = 0

    def __init__(self, name, start_height, start_age):
        self.name = name
        self.start_height = start_height
        self.start_age = start_age

        Plant.count += 1
        print(f"Created: {self.name}({self.start_height}cm, "
              f"{self.start_age} days)"
              )


print("=== Plant Factory Output ===")
Rose = Plant("Rose", 25, 30)
Oak = Plant("Oak", 200, 365)
Cactus = Plant("Cactus", 5, 90)
Sunflower = Plant("Sunflower", 80, 45)
Fern = Plant("Fern", 15, 120)
print("\nTotal plants created:", Plant.count)
