from typing import Any, Callable
import functools
import operator


# ── 1. spell_reducer ─────────────────────────────────────────────────────────

def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable] = {
        "add":      operator.add,
        "multiply": operator.mul,
        "max":      max,
        "min":      min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation '{operation}'. "
                         f"Supported: {list(ops)}")

    if not spells:
        return 0

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire":  functools.partial(base_enchantment, power=50, element="fire"),
        "ice":   functools.partial(base_enchantment, power=50, element="ice"),
        "storm": functools.partial(base_enchantment, power=50, element="storm")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


if __name__ == "__main__":

    # spell_reducer
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    # partial_enchanter
    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()}\
        enchantment (power={power}) on {target}"

    variants = partial_enchanter(base_enchantment)
    print(variants["fire"](target="Sword"))
    print(variants["ice"](target="Shield"))
    print(variants["storm"](target="Staff"))

    # memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    # spell_dispatcher
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))
