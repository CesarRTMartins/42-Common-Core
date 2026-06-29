from ex0.factory import CreatureFactory
from ex0.creature import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex1.healing_family import Sproutling
        return Sproutling()

    def create_evolved(self) -> Creature:
        from ex1.healing_family import Bloomelle
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex1.transform_family import Shiftling
        return Shiftling()

    def create_evolved(self) -> Creature:
        from ex1.transform_family import Morphagon
        return Morphagon()
