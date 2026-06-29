class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    Rose = Flower("Rose", 25, 30, "red")
    Papoila = Flower("Papoila", 10, 20, "azul")
    print(f"{Rose.name} ({Flower.__name__}): {Rose.height}cm, "
          f"{Rose.age} days, {Rose.color} color")
    Rose.bloom()
    ########################
    print("\n")
    Oak = Tree("Oak", 500, 1825, 50)
    Sobreiro = Tree("Sobreiro", 1000, 11625, 250)
    print(f"{Oak.name} ({Tree.__name__}): {Oak.height}cm, {Oak.age} "
          f"days, {Oak.trunk_diameter}cm diameter")
    Oak.produce_shade()
    ########################
    print("\n")
    Tomato = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")
    print(f"{Tomato.name} ({Vegetable.__name__}): {Tomato.height}cm, "
          f"{Tomato.age} days, {Tomato.harvest_season} harvest")
    Tomato.nutri_value()
