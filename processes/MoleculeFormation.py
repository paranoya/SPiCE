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
        #print(self.input.current_mass_Msun(),self.tau_Gyr,flux,'\n')
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
        self.tau_Gyr = self._formation_timescale()
        
    #---------------------
    #GETTING PHYSICAL PARAMETERS
    #---------------------
    def _dust_density(self):
        #total_H_density_cm3 = 0.5*self.agent.number_density() + self.input.number_density() + 2.*self.output.number_density()
        total_V_cm3 = self.agent.volume() + self.input.volume() + self.output.volume()
        total_H_density_cm3 = (0.5*self.agent.volume()/total_V_cm3)*self.agent.number_density() + (self.input.volume()/total_V_cm3)*self.input.number_density()+ (2.*self.output.volume()/total_V_cm3)*self.output.number_density()
        #print(total_H_density_cm3)
        return self._Z * total_H_density_cm3
    def _formation_timescale(self):
        #Taking Ascasibar+(in prep) formula again, ignoring the effective metallicity thing
        mean_ov_cm3_per_s = 6.e-17 * ((self.input.temperature()/100.)**(0.5)) #Neutral H or H2 temperature????
        #mean_ov_cm3_Gyr = 0.189*(self.input.temperature()/100.)**(0.5)
        
        tau_s = None #Not the correct tau unit-wise
        try:
            tau_s = 0.5/(mean_ov_cm3_per_s * self._dust_density())
        except ZeroDivisionError:
            tau_s = np.Infinity
        
        return tau_s*self._s_to_Gyr #Correct units.
    
    #---------------------
    #DEFINING USEFUL VARIABLES
    #---------------------
    def _constants(self):
        self._s_to_Gyr = ((1.*u.s).to(u.Gyr)).value