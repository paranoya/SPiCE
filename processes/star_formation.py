"""
Created on Wed Mar 27 10:30:28 2019

@author: yago
"""

from . import basic


# -----------------------------------------------------------------------------
class Constant_efficiency(basic.Process):

    def __init__(self, gas, stars, tau_SF):
        self.gas = gas  # gas phase that is converted into stars
        self.tau = tau_SF  # gas depletion time, in Gyr
        self.stars = stars  # destination stellar phase

    def compute_derivatives(self):
        SFR = self.gas.mass()/self.tau
        self.gas.update_derivatives(-SFR)
        self.stars.update_derivatives(SFR)

