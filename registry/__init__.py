from typing import Any, Callable

# registry: dict[str, Callable[[Any], Any]] = {}
registry: dict[str, dict[str, Any]] = {}


def register(
    year: int, day: int, part: int, completed: bool = False
) -> Callable[[Callable[[dict], Any]], Callable[[dict], Any]]:
    """Decorator to register a solution for a specific year, day, and part."""

    def decorator(func: Callable[[dict], None]) -> Callable[[dict], None]:
        key = f"year{year}_day{day:02d}_part{part}"
        registry[key] = {"func": func, "completed": completed}
        return func

    return decorator
