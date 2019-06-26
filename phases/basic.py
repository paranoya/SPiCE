#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

from astropy import units as u


# -----------------------------------------------------------------------------
class Phase:

    def __init__(self, model, params):
        self.model = model
        self.params = {**self.default_settings(), **params}
        self.current_mass = self.params['initial_mass_Msun']*u.Msun
        self.dm_dt = self.params['dm_dt_Msun_yr'] * u.Msun/u.yr

    def default_settings(self):
        return {
            'initial_mass_Msun': 0.,
            'dm_dt_Msun_yr': 0.
        }

    def mass(self):
        return self.current_mass

    def update_derivatives(self, term):
        self.dm_dt += term

    def get_timestep(self):
        self.dm_dt += self.model.integrator['relative_accuracy']*self.current_mass/self.dm_dt

    def update_mass(self, timestep):
        self.current_mass += self.dm_dt * timestep


# -----------------------------------------------------------------------------
class MultiphaseMedium(Phase):

    def __init__(self, model, params):
#        self.phases = phase_dict
        raise("TO DO: Multiphase medium to be implemented")

    def mass(self):
        m = 0.
        for phase in self.phases.values():
            m += phase.mass()
        return m

    def m(self, phase='total'):
        if(phase == 'total'):
            return self.mass()
        else:
            return self.phases[phase].mass()

    def update_derivatives(self, term):
        print("TO DO: estimate mass fractions")

    def __getitem__(self, key):
        return self.phases[key]
