#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:39:06 2019

@author: yago
"""

from astropy import units as u


# -----------------------------------------------------------------------------
class Process(object):

    def compute_derivatives():
        raise("ERROR: compute_derivatives method not implemented")


# -----------------------------------------------------------------------------
class Constant_timescale(Process):

    def __init__(self, model, params):
        self.input = model.phases[params['input_phase']]
        self.output = model.phases[params['output_phase']]
        self.tau = params['timescale_Gyr']*u.Gyr

    def compute_derivatives(self):
        flux = self.input.current_mass()/self.tau
        self.input.update_derivatives(-flux)
        self.output.update_derivatives(flux)
