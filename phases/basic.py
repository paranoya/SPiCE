#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

import numpy as np


# -----------------------------------------------------------------------------
class Phase:

    def __init__(self, model, params):
        self.model = model
        self.params = {**self.default_settings(), **params}
        self.mass_history_Msun = [float(self.params['initial_mass_Msun'])]

    def default_settings(self):
        return {
            'initial_mass_Msun': 0.,
        }

    def current_mass_Msun(self):
        return self.mass_history_Msun[-1]

    def mass(self, t):
        return np.interp(t, self.model.time, self.mass_history_Msun[-1])

    def reset_timestep(self):
        self.dm_dt_Msun_Gyr = 0.

    def update_derivatives(self, term):
        self.dm_dt_Msun_Gyr += term

    def get_timestep_Gyr(self):
        try:
            return np.abs((self.model.integrator['relative_accuracy']
                       * self.current_mass_Msun() / self.dm_dt_Msun_Gyr))
        except ZeroDivisionError:
            return np.Infinity

    def update_mass(self, timestep_Gyr):
        #Euler integrator is becoming a bottleneck, it should be replaced with a more efficient one.
        self.mass_history_Msun.append(self.current_mass_Msun()
                                      + self.dm_dt_Msun_Gyr*timestep_Gyr)


# -----------------------------------------------------------------------------
class MultiphaseMedium(Phase):

    def __init__(self, model, params):
#        self.phases = phase_dict
        raise("TO DO: Multiphase medium to be implemented")

    def mass(self):
        m = 0.
        for phase in self.phases.values():
            m += phase.current_mass_Msun()
        return m

    def m(self, phase='total'):
        if(phase == 'total'):
            return self.current_mass()
        else:
            return self.phases[phase].current_mass_Msun()

    def update_derivatives(self, term):
        print("TO DO: estimate mass fractions")

    def __getitem__(self, key):
        return self.phases[key]
