# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:43:38 2017

@author: yago
"""

from Ingredients import Ingredient
import numpy as np

# -----------------------------------------------------------------------------


class StellarEjecta(Ingredient):
    """
    Definition
    ----------
    **TODO: NOT VALID !!!**\n
    Fraction of the SSP mass with age :math:`\\tau` and metallicity :math:`Z`
    that is returned, per unit time, as element :math:`i`:\n
    :math:`\\dot R_i(\\tau,Z)
    = ~\\phi(m)~ \\frac{dm}{d \\tau}(\\tau)~ m_i(m,Z)`\n
    where :math:`m(\\tau)` is the mass of the star
    that dies after a time :math:`\\tau`
    and :math:`M_i` is the mass, in :math:`M_\\odot`,
    of element :math:`i` returned by the star.\n
    At any given time, this introduces a term\n
    :math:`E_i(t) \\equiv (\\dot M_i)_{ejecta}(t)
    = \\int_0^t \\Psi(t-\\tau)~\\dot R_i(\\tau,Z(t-\\tau))~ d\\tau`\n
    in the evolution equation for element :math:`i`.

    Usage
    -----
    blah
    """

    def m_returned(self, element, m, Z):
        """
        Return an array with the mass of `element` returned
        by stars with mass `m` and metallicity `Z`.
        """
        pass

# -----------------------------------------------------------------------------


class EjectaTable:
    """
    Table with ejecta for a given set of metallicities,
    each with its own set of stellar masses.\n
    """
    def __init__(self, Z_star, m_star, m_returned):
        """Input values 'by hand'"""
        self.Z_star = Z_star
        self.m_star = m_star
        self.m_returned = m_returned
#        TODO: Sanity checks (e.g. dimensions)

    def interpolate(m, Z):
        """ TODO: add bi-linear/log interpolation and (**WARNING**) extrapolation """


def iron_dust_INAF():
    """ TODO: add reference! """
    Z_star = np.array([3e-4, 1e-3, 8e-3, 1.8e-2])
    m_star = [np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5, 1.75, 2.0, 2.25,2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])]
    m_dust = [np.array([0.0,                  0.0,              0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0]),
              np.array([9.25e-8,          3.34e-9,          2.23e-9, 3.17e-8, 8.12e-6, 1.21e-5, 2.13e-5, 2.58e-5, 3.16e-5, 2.84e-5, 2.26e-5, 1.79e-5, 1.08e-5, 3.21e-6]),
              np.array([1.06e-5,          1.85e-5,          1.89e-6, 2.60e-6, 7.77e-5, 6.62e-5, 5.43e-5, 4.57e-5, 4.21e-5, 2.24e-5, 2.52e-5, 2.10e-5, 2.35e-5, 2.64e-5]),
              np.array([1.16e-4, 2.74e-4, 1.28e-3, 9.69e-5, 2.29e-5, 2.07e-5, 2.96e-4, 1.09e-4, 8.11e-5, 6.19e-5, 5.08e-5, 5.08e-5, 5.74e-5, 5.82e-5, 7.98e-5, 8.41e-5])]
    return EjectaTable(Z_star, m_star, m_dust)

class M18(StellarEjecta):
    """
    Millán et al. (2018)
    """
#    Implementation of Vital's method-based scheme:
#    def __init__(self, parameters):
#        """
#        One of the SPiCE parameters must be 'IMF',
#        and its value must correspond to one of the _*_shape() methods defined within this class,
#        to be called by the phi(m) method.
#        \n If the function _*_init() exists, it will be called once upon construction.
#        """
#        self.name = parameters.get('IMF','Undefined')
#        dummy = '_{}_shape'.format(self.name)
#        if(dummy in dir(self)):
#            self.shape = self.__class__.__dict__[dummy]
#            ... (rest of the constructor) ...
#        else:
#            print 'ERROR: IMF "{}" not defined'.format(self.name)
#            print dummy
#    

    def m_returned(self, element, m, Z):
        if(element == 'iron_dust'):
            return iron_dust_INAF().interpolate(m, Z)

# -----------------------------------------------------------------------------
