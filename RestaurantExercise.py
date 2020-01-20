# Restautant Exercise
menu = {
    'Brunch': {
        'Steak and Eggs': 16.99,
        'Three Egg Breakfast': 8.99,
        'Egg Benedict': 11.99,
        'Biscuit and Gravy': 7.99,
        'Chicken Fingers': 10.99,
        'Chicken Wrap': 8.99,
        'Steak Salad': 1.99
    },
    'Drinks': {
        'Soft Drink': 1.99,
        'Coffee': 1.99,
        'Orange Juice': 0.99,
        'Milk': 0.55,
        'Water': 0.00
    }
}

# Change 'Three Egg Breakfast' to have the options of: Withiut Bacon(8.99) and With Bacon(9.99)
menu['Brunch']['Three Egg Breakfast'] = {}
menu['Brunch']['Three Egg Breakfast']['Without Bacon'] = 8.99
menu['Brunch']['Three Egg Breakfast']['With Bacon'] = 9.99
#menu['Three Egg Breakfast']['Without Bacon'] = 8.99
#menu['Three Egg Breakfast']['With Bacon'] = 9.99
# Fix the price of the steak salad. It should be 15.99
menu['Steak Salad'] = 15.99
# Create new dictonary called Special Menu and add to menu dictonary.
menu['Special Menu'] = {}
# Added new keys and values to Special Menu dictonary
menu['Special Menu']['Soup of the Day'] = 8.99
menu['Special Menu']['Catch of the Day'] = 14.99
menu['Special Menu']['Chef Special'] = 15.99
print(menu)
