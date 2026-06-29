from abc import ABC, abstractmethod
from ex0.creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex0.flame_family import Flameling
        return Flameling()

    def create_evolved(self) -> Creature:
        from ex0.flame_family import Pyrodon
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex0.aqua_family import Aquabub
        return Aquabub()

    def create_evolved(self) -> Creature:
        from ex0.aqua_family import Torragon
        return Torragon()
