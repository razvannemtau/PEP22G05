shop1 = {'apples': 7.5, 'plums': 8.3, 'bread': 3.5}
shop2 = {'apples': 7.8, 'plums': 8.1, 'bread': 3.5}
shop3 = {'apples': 7.1, 'plums': 8.9, 'bread': 3.5}

shopping_cart = {'apples': 3, 'plums': 5, 'bread': 4}

shops = {'lid': shop1, 'kau': shop2, 'pro': shop3}
# what is the cheapest shop

result = {}
for shop_name, shop in shops.items():
    for product, quantity in shopping_cart.items():
        if result.get(shop_name):
            result.update({shop_name: (shop[product] * quantity) + result[shop_name]})
        else:
            result.update({shop_name: shop[product] * quantity})

print(result)