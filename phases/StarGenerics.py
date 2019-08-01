'''
Star classes

Mario Romero        May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
from . import basic

'''
PLACEHOLDER CLASS
Defined here to make photo-ionization and photo-dissociation processes work
'''
class Star(basic.Phase):
    
    #---------------------
    #DEFAULT SETTINGS
    #---------------------
    def __init__(self, model, params):
        #What everyone does
        self.model = model
        self.params = {**self.default_settings(), **params}
        self.mass_history_Msun = [float(self.params['initial_mass_Msun'])]
        self.SFR_history_Msun_per_Gyr = [] #It updates when a star formation process is called