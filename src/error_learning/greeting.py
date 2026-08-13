def build_greeting(name: str | None) -> str:
    resolved_name = "guest" if name is None else name
    return f"Hello, {resolved_name}!"
