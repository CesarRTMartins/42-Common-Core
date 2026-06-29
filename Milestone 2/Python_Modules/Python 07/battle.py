from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory_a: CreatureFactory,
                factory_b: CreatureFactory) -> None:
    print("Testing battle")
    a = factory_a.create_base()
    b = factory_b.create_base()

    print(f"{a.describe()} vs. {b.describe()} fight!")
    print(a.attack())
    print(b.attack())


flame = FlameFactory()
aqua = AquaFactory()

test_factory(flame)
test_factory(aqua)
test_battle(flame, aqua)
