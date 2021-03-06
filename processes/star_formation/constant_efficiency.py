#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:30:28 2019

@author: yago
"""


# -----------------------------------------------------------------------------
class Process(object):

    def compute_derivatives():
        raise("ERROR: compute_derivatives method not implemented")


# -----------------------------------------------------------------------------
class Constant_efficiency(Process):

    def __init__(self, gas, stars, tau_SF):
        self.gas = gas  # gas phase that is converted into stars
        self.tau = tau_SF  # gas depletion time, in Gyr
        self.stars = stars  # destination stellar phase

    def compute_derivatives(self):
        SFR = self.gas.mass()/self.tau
        self.gas.update_derivatives(-SFR)
        self.stars.update_derivatives(SFR)
