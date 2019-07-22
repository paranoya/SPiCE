#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processes related with formation of molecules

Mario Romero           July 2019
"""

import numpy as np
import astropy.units as u
from . import basic

'''
Hydrogen molecule creation
H -> H2 process
'''
class MolecularHydrogen_Formation(basic.Process):
    
    #---------------------
    #INIT
    #---------------------
    def __init__(self, model, params):
        self.input = model.phases[params['input_phase']]   #Neutral Hydrogen
        self.output = model.phases[params['output_phase']] #Molecular Hydrogen
        self.agent = model.phases[params['agent_phase']] #Ionized Hydrogen
        self._Z = float(params['metallicity'])
        
        self._constants()
        self.tau_Gyr = self._formation_timescale()
    
    def compute_derivatives(self):
        flux = self.input.current_mass_Msun()/self.tau_Gyr
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
    #---------------------
    #GETTING PHYSICAL PARAMETERS
    #---------------------
    def _dust_density(self):
        total_H_density = 0.5*self.agent.number_density() + self.input.number_density() + 2.*self.output.number_density()
        return self._Z * total_H_density
    def _formation_timescale(self):
        #Taking Ascasibar+(in prep) formula again, ignoring the effective metallicity thing
        mean_ov_cm3_s = 6.e-17 *(self.input.temperature()/100.)**(0.5) #Neutral H or H2 temperature????
        
        tau_s = None #Not the correct tau unit-wise
        try:
            tau_s = 0.5/(mean_ov_cm3_s * self._dust_density())
        except ZeroDivisionError:
            tau_s = np.Infinity
        
        return tau_s*self._s_to_Gyr #Correct units.
    #---------------------
    #DEFINING USEFUL VARIABLES
    #---------------------
    def _constants(self):
        self._s_to_Gyr = ((1.*u.s).to(u.Gyr)).value