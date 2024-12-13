from typing import Any, Callable

registry: dict[str, Callable[[Any], Any]] = {}


def register(
    year: int, day: int, part: int
) -> Callable[[Callable[[dict], None]], Callable[[dict], None]]:
    """Decorator to register a solution for a specific year, day, and part."""

    def decorator(func: Callable[[dict], None]) -> Callable[[dict], None]:
        key = f"year{year}_day{day:02d}_part{part}"
        registry[key] = func
        return func

    return decorator
