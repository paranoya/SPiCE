#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:39:06 2019

@author: yago
"""


# -----------------------------------------------------------------------------
class Process(object):

    def compute_derivatives():
        raise("ERROR: compute_derivatives method not implemented")


# -----------------------------------------------------------------------------
class Constant_timescale(Process):

    def __init__(self, model, params):
        self.input = model.phases[params['input_phase']]
        self.output = model.phases[params['output_phase']]
        self.tau_Gyr = float(params['timescale_Gyr'])

    def compute_derivatives(self):
        flux = self.input.current_mass_Msun()/self.tau_Gyr
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
        #PLACEHOLDER! This will fail if two processes give an SFR as main result
        self.output.SFR_history_Msun_per_Gyr.append(flux)
