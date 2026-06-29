class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(self.name, ': ', self.height, " cm, ", self.age,
              " days old", sep='')

    def grow(self):
        self.height = self.height + 1

    def aging(self):
        self.age = self.age + 1

    def dev(self):
        self.grow()
        self.aging()


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Cactus = Plant("Cactus", 40, 120)
    Cannabis = Plant("Cannabis", 10, 20)

    list = [Rose, Cactus, Cannabis]
    for i in range(1, 8):
        print("=== Day ", i, " ===", sep='')
        for n in list:
            n.dev()
            n.get_info()
    print("Growth this week: +6cm")
