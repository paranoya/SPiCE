#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processes related with recombination

Mario Romero           July 2019
"""

import numpy as np
import astropy.units as u
from . import basic

'''
Hydrogen Recombination
HI -> H process
'''
class Hydrogen_Recombination(basic.Process):
    
    #---------------------
    #INIT
    #---------------------
    def __init__(self, model, params):
        self.input = model.phases[params['input_phase']]   #Ionized Hydrogen
        self.output = model.phases[params['output_phase']] #Neutral Hydrogen
        
        self._constants()
        self.tau_Gyr = self._recombination_timescale()
    
    def compute_derivatives(self):
        flux = self.input.current_mass_Msun()/self.tau_Gyr
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
    #---------------------
    #GETTING THE TAU
    #---------------------
    def _recombination_timescale(self):
        #Taking Ascasibar+(in prep) formula
        mean_ov_cm3_s = 4.1e-10 * (self.input.temperature())**(-0.8) #Case B recombination cross-section (Verner&Ferland 96)
        
        tau_s = None #Not the correct tau unit-wise
        try:
            tau_s = 2./(mean_ov_cm3_s * self.input.number_density())
        except ZeroDivisionError:
            tau_s = np.Infinity
        
        return tau_s*self._s_to_Gyr #Correct units.
    #---------------------
    #DEFINING USEFUL VARIABLES
    #---------------------
    def _constants(self):
        self._s_to_Gyr = ((1.*u.s).to(u.Gyr)).value