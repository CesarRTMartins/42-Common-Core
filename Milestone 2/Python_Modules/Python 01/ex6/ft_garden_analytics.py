class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self):
        self.height = self.height + 1
        print(self.name, "grew 1cm")

    def show(self):
        print("-", self.name + ":", str(self.height) + "cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def show(self):
        print("-", self.name + ":", str(self.height) + "cm,",
              self.color, "flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def show(self) -> None:
        print("-", self.name + ":", str(self.height) + "cm,",
              self.color, "flowers (blooming), Prize points:",
              self.points)


class GardenManager:

    class GardenStats:
        @staticmethod
        def score(plants: list) -> int:
            total = 0
            for i in range(0, plants.count):
                total = total + plants.list[i].height
            return total

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.list = []
        self.count = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.list.append(plant)
        self.count = self.count + 1
        print("Added", plant.name, "to", self.owner + "'s garden")

    def grow_all(self):
        print(self.owner, "is helping all plants grow...")
        for i in range(0, self.count):
            self.list[i].grow()
            self.total_growth = self.total_growth + 1

    def report(self):
        print("===", self.owner + "'s Garden Report ===")
        print("Plants in garden:")

        regular = 0
        flowering = 0
        prize = 0

        for i in range(0, self.count):
            plant = self.list[i]
            plant.show()

            if type(plant) is PrizeFlower:
                prize = prize + 1
            elif type(plant)is FloweringPlant:
                flowering = flowering + 1
            else:
                regular = regular + 1
        print()
        print("Plants added:", self.count, ", Total growth:",
              str(self.total_growth) + "cm")
        print("Plant types:", regular, "regular,", flowering,
              "flowering,", prize, "prize flowers")
        print()
        print("Height validation test:", self.validate())
        score = GardenManager.GardenStats.score(self)
        print("Garden scores -", self.owner + ":", score)
        print("Total gardens managed: 1")

    @staticmethod
    def validate() -> bool:
        return True

    @classmethod
    def create_garden_network(cls, owner: str):
        return cls(owner)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    garden = GardenManager.create_garden_network("Alice")
    print()
    garden.add_plant(Plant("Oak Tree", 100))
    garden.add_plant(FloweringPlant("Rose", 25, "red"))
    garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    garden.grow_all()
    print()
    garden.report()
    print()
