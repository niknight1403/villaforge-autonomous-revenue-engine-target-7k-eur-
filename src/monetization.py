def calculate_mrr(users: int, price: float) -> float:
    if users < 0 or price < 0:
        raise ValueError('Inputs must be non-negative')
    return float(users * price)