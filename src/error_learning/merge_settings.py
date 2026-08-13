from typing import Any


def merge_settings(current: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    return current | patch
