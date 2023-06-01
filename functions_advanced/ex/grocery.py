def grocery_store(**food_items):
    sorted_grocery = sorted(food_items.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return '\n'.join([f"{p}: {q}" for p, q in sorted_grocery])

