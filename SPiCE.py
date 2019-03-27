#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

from simple_model import gas, stars
from star_formation import constant_efficiency as SF


# -----------------------------------------------------------------------------
def read_parameter_file(file_name):
    print("Reading parameters from '{}'".format(file_name))
    parameters = {}
    with open(file_name) as parameter_file:
        for line in parameter_file:
            words = line.split(None, 2)
            if(len(words) > 1 and words[0][0] != '#'):
                parameters[words[0]] = words[1]
    return parameters


# <codecell> Initialisation

run_parameters = read_parameter_file('parameters.txt')
phases = [gas, stars]
processes = [SF]

for phase in phases:
    phase.init(run_parameters)

for process in processes:
    process.compute_derivatives()


# <codecell> Main loop

for phase in phases:
    print(phase.current_state, phase.derivatives)


# -----------------------------------------------------------------------------
#                                                    ... Paranoy@ Rulz! ;^D
# -----------------------------------------------------------------------------
