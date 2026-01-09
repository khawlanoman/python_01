class Plant:
    def __init__(self,name,height,Age):
        self.name = name
        self.height = height
        self.Age = Age

    def age(self):
       self.Age +=1
    def grow(self):
        self.height +=1
    def get_info(self):
        print(self.name,":",self.height,"cm,", self.Age,"days old")

if __name__ == "__main__":
    Rose = Plant("Rose",25,30)
    i = 0;
    count = 0
    print("=== Day 1 ===")
    Rose.get_info()
    while (i < 7):
        if(i == 6):
            print("=== Day 7 ===")
            Rose.get_info()
            break
        Rose.grow()
        Rose.age()
        count +=1
        i +=1
    print("Growth this week:",count, "cm")

