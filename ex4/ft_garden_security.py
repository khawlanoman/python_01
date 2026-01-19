class SecurePlant:
    """this class to secure we plants"""
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        """methode get_height is for  return the height value  """
        return (self._height)

    def get_age(self):
        """methode get_age is for  return the age value  """
        return (self._age)

    def set_height(self, height):
        """methode set_height is for  change and check height value  """
        if height < 0:
            print("Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        elif height >= 0:
            self._height = height

    def set_age(self, age):
        """methode set_age is for change and check age value  """
        if age < 0:
            print(f"Invalid operation attempted:age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        elif age >= 0:
            self._age = age


print("=== Garden Security System ===")
Rose = SecurePlant("Rose", 25, 30)
print(f"Plant created: {Rose.name}")
print(f"Height updated:{Rose._height}cm [ok]")
print(f"Age updated:{Rose._age} days[ok]")
print("\n")
Rose.set_height(-5)
print(f"\nplant: {Rose.name} ({Rose._height}cm {Rose._age} days) ")
