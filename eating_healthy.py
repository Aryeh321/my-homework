import json

def eating_proper(vegetables, vegetable_N, forbidden_candy):
    formatted_list = ', '.join(vegetables)
    formatted_list_2 = ', '.join(forbidden_candy)
    
    return f"I make my kids eat {formatted_list} and even {vegetable_N}, but would never let them eat {formatted_list_2}."

with open('kids_foods.json', 'r') as f:
    data = json.load(f)

output = eating_proper(data['vegetables'], data['vegetable_N'], data['forbidden_candy'])

print(output)