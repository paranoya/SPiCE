# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:29:36 2017

@author: yago
"""

from Ingredients import *
from IMFs import IMF
from Ejecta import StellarEjecta
#-------------------------------------------------------------------------------

class SSP_m_min(FloatNumber):
    """
    Minimum mass of a star, in :math:`M_\\odot`\n
    :math:`\\log(m_i) = \\log(m_{min}) + \\frac{i}{m_{steps}-1}\\log(\\frac{m_{max}}{m_{min}})`
    """
    minimum_allowed = 0.001
    maximum_allowed = 1.0
    default_value = 0.01

class SSP_m_max(FloatNumber):
    """
    Maximum mass of a star, in :math:`M_\\odot`\n
    :math:`\\log(m_i) = \\log(m_{min}) + \\frac{i}{m_{steps}-1}\\log(\\frac{m_{max}}{m_{min}})`
    """
    minimum_allowed = 1.0
    maximum_allowed = 1000
    default_value = 100

class SSP_m_steps(IntNumber):
    """
    Number of stellar masses in array,\n
    :math:`\\log(m_i) = \\log(m_{min}) + \\frac{i}{m_{steps}-1}\\log(\\frac{m_{max}}{m_{min}})`
    """
    minimum_allowed = 100
    maximum_allowed = 10000
    default_value = 400

class SSP_Z_steps(IntNumber):
    """
    Number of stellar metallicities in array,\n
    :math:`Z_i = \\left( \\frac{i}{m_{steps}-1} \\right)^8`
    """
    minimum_allowed = 20
    maximum_allowed = 1000
    default_value = 100

class SSP(Ingredient):
    """ Simple Stellar Population """
    contains_ingredient_classes = [SSP_m_min, SSP_m_max, SSP_m_steps, SSP_Z_steps, IMF, StellarEjecta]

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
