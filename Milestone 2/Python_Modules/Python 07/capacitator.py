from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability

print("Testing Creature with healing capability")
heal_factory = HealingCreatureFactory()

for label, creature in [("base", heal_factory.create_base()),
                        ("evolved", heal_factory.create_evolved())]:
    print(f"{label}:")
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())

print()
print("Testing Creature with transform capability")
transform_factory = TransformCreatureFactory()

for label, creature in [("base", transform_factory.create_base()),
                        ("evolved", transform_factory.create_evolved())]:
    print(f"{label}:")
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
