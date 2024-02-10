# from collections import defaultdict
#
# transactions = [
#     {"product": "Apple", "quantity": 4, "price_per_unit": 0.30},
#     {"product": "Apple", "quantity": 2, "price_per_unit": 0.30},
#     {"product": "Banana", "quantity": 2, "price_per_unit": 0.50},
#     {"product": "Banana", "quantity": 3, "price_per_unit": 0.50},
#     {"product": "Orange", "quantity": 6, "price_per_unit": 0.40},
#     {"product": "Orange", "quantity": 2, "price_per_unit": 0.40},
#     {"product": "Mango", "quantity": 5, "price_per_unit": 0.70},
#     {"product": "Mango", "quantity": 3, "price_per_unit": 0.70},
#     {"product": "Grapes", "quantity": 3, "price_per_unit": 0.20},
#     {"product": "Grapes", "quantity": 4, "price_per_unit": 0.20},
#     {"product": "Peach", "quantity": 6, "price_per_unit": 0.60},
#     {"product": "Peach", "quantity": 2, "price_per_unit": 0.60}
# ]
# product_totals = defaultdict(float)
#
# for transaction in transactions:
#     product = transaction["product"]
#     quantity = transaction["quantity"]
#     price_per_unit = transaction["price_per_unit"]
#     total_price = quantity * price_per_unit
#     product_totals[product] += total_price
#
# result_dict = dict(product_totals)
#
# print(result_dict)

s= "tree"
new = s.count("t")
print(new)
output = ""
dict_count = {}
for i in s:
    dict_count[i]+=(s.count(i))
print(dict_count)
