# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:29:36 2017

@author: yago
"""

from Ingredients import Ingredient
from IMFs import IMF
#-------------------------------------------------------------------------------

class SSP(Ingredient):
    """ Simple Stellar Population """
    contains_ingredient_classes = [IMF]

#-------------------------------------------------------------------------------

class SPiCE_model(Ingredient):
    """ Main class """
    contains_ingredient_classes = [SSP]
    
#model = SPiCE_model({'IMF':'Salpeter', 'Salpeter_m_min':'0.01'})
model = SPiCE_model.from_file('ingredients.txt')
model.info()

#-------------------------------------------------------------------------------

#        
#        self._IMF = IMF(self._parameters)
#
#-------------------------------------------------------------------------------
