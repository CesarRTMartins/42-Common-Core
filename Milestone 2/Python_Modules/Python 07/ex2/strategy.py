from abc import ABC, abstractmethod
from typing import Protocol, TypeGuard
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class TransformableCreature(Protocol):
    def attack(self) -> str:
        ...

    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class HealableCreature(Protocol):
    def attack(self) -> str:
        ...

    def heal(self, target: str = "itself") -> str:
        ...


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> TypeGuard[TransformableCreature]:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature ' \
                            {creature.name}' for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> TypeGuard[HealableCreature]:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature ' \
                                {creature.name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())
