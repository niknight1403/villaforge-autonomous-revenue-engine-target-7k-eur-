def calculate_mrr(users, price):
    if users < 0 or price < 0:
        raise ValueError('Users and price must be non-negative')
    return users * price