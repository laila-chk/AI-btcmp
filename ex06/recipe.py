cookbook = {
        'Sandwich' : {'ingredients':['ham', 'bread', 'cheese', 'tomatoes'] , 'meal': 'launch', 'prep_time':10},
        'Cake' : {'ingredients': ['flour', 'sugar', 'eggs'] , 'meal': 'dessert', 'prep_time' : 60},
        'Salad' : {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'] , 'meal' : 'lunch' , 'prep_time':15}
        }
def recipes():
    for key in cookbook:
        print(key)
def rec_details(recipe):
    print(type(str(cookbook.items())))
    for recp, inf in cookbook.items():
        if str(recipe) is str(cookbook.items()):
            print("kaaaayn!")
rec_details('Cake')
