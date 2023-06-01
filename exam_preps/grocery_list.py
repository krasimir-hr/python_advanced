def shop_from_grocery_list(budget, grocery_list, *product_prices):
    items_bought = []
    for product, price in product_prices:
        if product in grocery_list and product not in items_bought:
            if price > budget:
                break
            items_bought.append(product)
            grocery_list.remove(product)
            budget -= price
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


