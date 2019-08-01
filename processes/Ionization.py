#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processes related with ionization proccesses

Mario Romero           July 2019
"""

import numpy as np
import astropy.units as u
from . import basic

'''
Hydrogen Photoionization
HI -> HII process
'''
class Basic_Photoionization(basic.Process):
    
    #---------------------
    #INIT
    #---------------------
    def __init__(self, model, params):
        self.input = model.phases[params['input_phase']]
        self.output = model.phases[params['output_phase']] 
        self.agent = model.phases[params['agent_phase']]  #Stars
        self._eff = float(params['efficiency']) #=Mass of photoionized gas per Mass of stars
    
    def compute_derivatives(self):
        #flux = self.input.current_mass_Msun()/self.tau_Gyr
        try:
            flux = self._eff * self.agent.SFR_history_Msun_per_Gyr[-1]
        except IndexError:
            flux = 0.0
        #print(self.agent.SFR_history_Msun_per_Gyr[0])
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
        
        try:
            self.tau_Gyr = self.input.current_mass_Msun() / flux
        except (FloatingPointError,ZeroDivisionError):
            self.tau_Gyr = np.Infinity
        #print(self.model.input)