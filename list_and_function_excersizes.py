def veggie_variety(vegetable, vegetable_N, forbidden_candy):
    
    formatted_list = ', '.join(vegetable)
    formatted_list_2 = ', '.join(forbidden_candy)
    return f"I make my kids eat {formatted_list} and even {vegetable_N}, but would never let them eat {formatted_list_2}."

veggie_list = ['carrot', 'broccoli', 'pepper', 'onion', 'tomato', 'mushroom']
vegetable_N = 'spinach'
forbidden_candy = ['lollies', 'taffies']

print(veggie_variety(veggie_list[3:6], vegetable_N, forbidden_candy))