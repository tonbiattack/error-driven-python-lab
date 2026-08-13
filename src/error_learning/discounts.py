def discount_for(code: str, discounts: dict[str, int]) -> int:
    return discounts.get(code, 0)
