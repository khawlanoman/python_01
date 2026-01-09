class SecurePlant:
    def __init__(self,name,height,age):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
      return (self._height)

    def get_age(self):
      return (self._age)

    def set_height(self, height):
      if height < 0:
        print(f"Invalid operation attempted: height {height} cm [REJECTED]")
        print(f"Security: Negative height rejected")
        return
      elif height >= 0:
        self._height = height

    def set_age(self, age):
      if age <0:
        print(f"Invalid operation attempted:age {age} days [REJECTED]")
        print(f"Security: Negative age rejected")
        return
      elif age >= 0:
        self._age =age


if __name__ == "__main__":

  print("=== Garden Security System ===")
  
  Rose= SecurePlant("Rose",25, 30)
  print(f"Plant created: {Rose.name}")
  print(f"Height updated:{Rose._height}cm [ok]")
  print(f"Age updated:{Rose._age} days[ok]")
  print("\n")
  Rose.set_height(-5)

  print(f"\nplant: {Rose.name} ({Rose._height}cm {Rose._age} days) ")
 
