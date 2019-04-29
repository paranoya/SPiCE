#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division


# -----------------------------------------------------------------------------
class Phase:

    def __init__(self, params):
        self.params = {**self.default_settings(), **params}

    def mass(self):
        return self.params['current_mass']

    def update_derivatives(self, term):
        self.params['dm_dt'] += term

    def default_settings(self):
        return {
            'current_mass': 0.,
            'dm_dt': 0.
        }


# -----------------------------------------------------------------------------
class MultiphaseMedium(Phase):

    def __init__(self, phase_dict={}):
        self.phases = phase_dict

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
