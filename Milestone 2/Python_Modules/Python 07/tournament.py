from typing import List, Tuple
from ex0.factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures = [(factory.create_base(), strategy)
                 for factory, strategy in opponents]

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature_a, strategy_a = creatures[i]
            creature_b, strategy_b = creatures[j]

            print("* Battle *")
            print(f"{creature_a.describe()} vs. \
                    {creature_b.describe()} now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


# Tournament 0 — basic
print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
battle([
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
])

print()

# Tournament 1 — error (Flameling has no TransformCapability)
print("Tournament 1 (error)")
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
battle([
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
])

print()

# Tournament 2 — multiple opponents
print("Tournament 2 (multiple)")
print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
battle([
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy()),
])
