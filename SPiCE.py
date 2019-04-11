#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

import phases


# -----------------------------------------------------------------------------
class Model(phases.basic_phases.MultiphaseMedium):

    def __init__(self, parameter_file):
        print("Reading parameters from '{}'".format(parameter_file))
        self.parameters = {}
        with open(parameter_file) as f:
            for line in f:
                words = line.split(None, 2)
                if(len(words) > 1 and words[0][0] != '#'):
                    self.parameters[words[0]] = words[1]
        self.phases = {}
        self.phases['gas'] = phases.basic_phases.Phase(
                float(self.parameters.get('initial_gas_mass', 0.)))
        self.phases['stars'] = phases.basic_phases.Phase(
                float(self.parameters.get('initial_stellar_mass', 0.)))

    def update_derivatives(self, term):
        print("This should not happen!")
        raise(-1)


# <codecell> Initialisation

model = Model('parameters.txt')
print(model.mass(), model.m('gas'), model.m('stars'), model.m('total'))
print(model['gas'].mass())

# -----------------------------------------------------------------------------
#                                                    ... Paranoy@ Rulz! ;^D
# -----------------------------------------------------------------------------
