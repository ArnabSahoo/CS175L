#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#CS175

#Arnab Sahoo

#restaurant


vegetarian = input('Is anyone in your party vegetarian? (Yes or No): ')
vegan = input('Is anyone in your party vegan? (Yes or No): ')
gluten_free = input('Is anyone in your party gluten-free? (Yes or No): ')

if vegetarian == 'Yes':
    if vegan == 'Yes':
        if gluten_free == 'Yes':
            print ('\nHere are your resturant choices.\nCorner Café\nThe Chef\'s Kitchen')

if vegetarian == 'Yes':
    if vegan == 'No':
        if gluten_free == 'No':
            print ('\nHere are your resturant choices.\nMama\'s Fine Italian\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
            
if vegetarian == 'Yes':
    if vegan == 'No':
        if gluten_free == 'Yes':
            print ('\nHere are your resturant choices.\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')

if vegetarian == 'Yes':
    if vegan == 'Yes':
        if gluten_free == 'No':
            print ('\nHere are your resturant choices.\nCorner Café\nThe Chef\'s Kitchen')
   
if vegetarian == 'No':
    if vegan == 'No':
        if gluten_free == 'No':
            print ('\nHere are your resturant choices.\nJoe\'s Gourmet Burgers\nMama\'s Fine Italian\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
            
if vegetarian == 'No':
    if vegan == 'No':
        if gluten_free == 'Yes':
            print ('\nHere are your resturant choices.\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
            
if vegetarian == 'No':
    if vegan == 'Yes':
        if gluten_free == 'Yes':
            print ('\nHere are your resturant choices.\nCorner Café\nThe Chef\'s Kitchen')
            
if vegetarian == 'No':
    if vegan == 'Yes':
        if gluten_free == 'No':
            print ('\nHere are your resturant choices.\nCorner Café\nThe Chef\'s Kitchen')
            
