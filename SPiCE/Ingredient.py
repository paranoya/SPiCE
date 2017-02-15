# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:29:36 2017

@author: yago
"""
#-------------------------------------------------------------------------------

class Ingredient(object):
    """ Generic base class """
    
    ingredients = []
    
    @classmethod
    def add_ingredient(cls, ingredient):
        cls.ingredients.append(ingredient)
    
    def __init__(self, parameters):
        self.instances = []
    
    @classmethod
    def create(cls, parameters):
        print 'This class:', cls.__name__
        print 'Subclasses:', cls.__subclasses__()
        print 'Ingredients:', cls.ingredients
#        for ingredient in ingredients:
#            instances += ingredient.create(parameters)
    
#-------------------------------------------------------------------------------
