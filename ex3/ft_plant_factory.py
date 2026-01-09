class Plant:
    count = 0
    def __init__(self,name,start_height,start_age):
        self.name = name
        self.start_height  = start_height
        self.start_age = start_age

        Plant.count +=1
        print("Created:",self.name,"(",self.start_height,"cm,", self.start_age,"days)")

if __name__ == "__main__":
    Rose= Plant("Rose",25, 30)
    Oak = Plant("Oak",200, 365)
    Cactus = Plant("Cactus",5, 90)
    Sunflower =Plant("Sunflower",80, 45)
    Fern =Plant("Fern",15, 120)
    print("\nTotal plants created:" ,Plant.count)
