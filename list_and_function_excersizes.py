def veggie_variety(vegetable, vegetable_N):
    
    formatted_list = ', '.join(vegetable)
    return f"I make my kids eat {formatted_list} and even {vegetable_N}"

veggie_list = ['carrot', 'broccoli', 'pepper', 'onion', 'tomato', 'mushroom']
vegetable_N = 'spinach'

print(veggie_variety(veggie_list[3:6], vegetable_N))