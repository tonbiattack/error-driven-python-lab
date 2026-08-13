from typing import Any


def merge_settings(current: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    result = current.copy()

    for key, value in patch.items():
        existing = result.get(key)
        if isinstance(existing, dict) and isinstance(value, dict):
            result[key] = merge_settings(existing, value)
        else:
            result[key] = value

    return result
