class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def create(plants_data) -> list:
        plants = []
        for name, height, age in plants_data:
            plants.append(Plant(name, height, age))
        return plants


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    created_plants = Plant.create(plants)
    counter = 0
    for n in created_plants:
        counter = counter + 1
        print(f"Created: {n.name} ({n.height}cm, {n.age} days)")
    print()
    print("Total plants created:", counter)
