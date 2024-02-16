#CS175

#Arnab Sahoo

#restaurant

def restaurant_search():
    while True:
        vegetarian = input('Is anyone in your party vegetarian? (Yes or No): ')
        vegan = input('Is anyone in your party vegan? (Yes or No): ')
        gluten_free = input('Is anyone in your party gluten-free? (Yes or No): ')

        print('\nHere are your restaurant choices:')

        if vegetarian == 'Yes':
            if vegan == 'Yes':
                if gluten_free == 'Yes':
                    print('Corner Café\nThe Chef\'s Kitchen')
                else:
                    print('Corner Café\nThe Chef\'s Kitchen')
            else:
                if gluten_free == 'Yes':
                    print('Main Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
                else:
                    print('Mama\'s Fine Italian\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
        else:
            if vegan == 'No':
                if gluten_free == 'No':
                    print('Joe\'s Gourmet Burgers\nMama\'s Fine Italian\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
                else:
                    print('Main Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
            else:
                if gluten_free == 'Yes':
                    print('Corner Café\nThe Chef\'s Kitchen')
                else:
                    print('Corner Café\nThe Chef\'s Kitchen')

        another_search = input('\nEnter \'yes\' if you would like to do another restaurant search (enter \'no\' to end): ')
        if another_search.lower() != 'yes':
            break

restaurant_search()
