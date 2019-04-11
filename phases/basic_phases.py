#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division


# -----------------------------------------------------------------------------
class Phase(object):

    def __init__(self, initial_mass=0.):
        self.current_mass = initial_mass
        self.dm_dt = 0.

    def mass(self):
        return self.current_mass

    def update_derivatives(self, term):
        self.dm_dt += term


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


print('hello')

# -----------------------------------------------------------------------------
#                                                    ... Paranoy@ Rulz! ;^D
# -----------------------------------------------------------------------------
