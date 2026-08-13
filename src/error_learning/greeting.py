def build_greeting(name: str | None) -> str:
    return f"Hello, {name or 'guest'}!"
