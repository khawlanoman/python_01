class Plant:
    """ this class  for create the  plant objects  """
    def __init__(self, name, height, Age):
        self.name = name
        self.height = height
        self.Age = Age

    def age(self):
        """ this methode for increment  the age  """
        self.Age += 1

    def grow(self):
        """this methode for increment the height """
        self.height += 1

    def get_info(self):
        """ get_info is a methode that shows the the plant growth status """
        print(self.name, ":", self.height, "cm,", self.Age, "days old")


Rose = Plant("Rose", 25, 30)
i = 0
count = 0
print("=== Day 1 ===")
Rose.get_info()
while (i < 7):
    if (i == 6):
        print("=== Day 7 ===")
        Rose.get_info()
        break
    Rose.grow()
    Rose.age()
    count += 1
    i += 1
print("Growth this week: +", count, "cm")
