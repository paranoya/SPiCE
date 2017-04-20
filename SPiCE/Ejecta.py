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
    """ Papers used to complete this table:
        :math:`Z= 3 10^{-4}  Di Criscienzo et al. MNRAS. 433, 313-323.(2013)\n
        :math:`Z= 10^{-3}  Ventura et al. MNRAS. 420, 1442–1456. (2012) \n
        :math:`Z= 8 10^{-3} Ventura et al. MNRAS 424, 2345-2357. (2012) \n
        :math:`Z= 1.8 10^{-2} Dell’Agli et al. MNRAS 467, 4431-4440. (2017) \n
    
    """
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

def olivine_dust_INAF():
    """ :math:`Z= 3 10^{-4}  Di Criscienzo et al. MNRAS. 433, 313-323.(2013)\n
        :math:`Z= 10^{-3}  Ventura et al. MNRAS. 420, 1442–1456. (2012) \n
        :math:`Z= 8 10^{-3} Ventura et al. MNRAS 424, 2345-2357. (2012) \n
        :math:`Z= 1.8 10^{-2} Dell’Agli et al. MNRAS 467, 4431-4440. (2017) \n
    
    """
    Z_star = np.array([3e-4, 1e-3, 8e-3, 1.8e-2])
    m_star = [np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5, 1.75, 2.0, 2.25,2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])]
    m_dust = [np.array([0.0,                  0.0,              0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0]),
              np.array([4.97e-7,          6.19e-9,          1.97e-7, 8.50e-8, 7.40e-5, 7.22e-5, 3.55e-5, 2.66e-5, 5.18e-5, 1.11e-4, 1.94e-4, 2.97e-4, 4.14e-4, 6.11e-4]),
              np.array([4.97e-7,          1.01e-12,         5.46e-7, 7.54e-7, 1.03e-3, 1.44e-3, 1.87e-3, 2.20e-3, 2.50e-3, 3.47e-3, 4.07e-3, 5.49e-3, 5.82e-3, 6.11e-3]),
              np.array([8.45e-5, 2.81e-5, 6.36e-6, 1.81e-6, 1.62e-7, 5.24e-7, 1.53e-3, 2.33e-3, 2.75e-3, 3.31e-3, 3.91e-3, 4.47e-3, 5.60e-3, 5.92e-3, 7.51e-3, 8.22e-3])]
    
    return EjectaTable(Z_star, m_star, m_dust)

def pyroxene_dust_INAF():
    """ :math:`Z= 3 10^{-4}  Di Criscienzo et al. MNRAS. 433, 313-323.(2013)\n
        :math:`Z= 10^{-3}  Ventura et al. MNRAS. 420, 1442–1456. (2012) \n
        :math:`Z= 8 10^{-3} Ventura et al. MNRAS 424, 2345-2357. (2012) \n
        :math:`Z= 1.8 10^{-2} Dell’Agli et al. MNRAS 467, 4431-4440. (2017) \n
    
    """
    Z_star = np.array([3e-4, 1e-3, 8e-3, 1.8e-2])
    m_star = [np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5,       2.0,      2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]),
              np.array([1.5, 1.75, 2.0, 2.25,2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])]
    m_dust = [np.array([0.0,                  0.0,              0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0,     0.0]),
              np.array([1.89e-7,           2.88e-9,         9.68e-10, 3.50e-8, 2.63e-5, 2.70e-5, 2.12e-5, 1.31e-5, 2.53e-5, 5.04e-5, 7.29e-5, 7.81e-5, 7.33e-5, 8.02e-5]),
              np.array([1.89e-7,          6.72e-13,         2.06e-7, 3.95e-7, 3.22e-4, 4.19e-4, 5.00e-4, 5.53e-4, 5.88e-4, 6.16e-4, 5.93e-4, 5.68e-4, 5.76e-4, 6.40e-4]),
              np.array([2.95e-5,1.18e-5,2.36e-6,7.05e-7,6.06e-8,2.08e-7,4.44e-4,6.00e-4,6.74e-4,7.70e-4,8.70e-4,9.61e-4,1.12e-3,1.16e-3,1.36e-3,1.43e-3])]
    
    return EjectaTable(Z_star, m_star, m_dust)

def carbon_dust_INAF():
    """ :math:`Z= 3 10^{-4}  Di Criscienzo et al. MNRAS. 433, 313-323.(2013)\n
        :math:`Z= 10^{-3}  Ventura et al. MNRAS. 420, 1442–1456. (2012) \n
        :math:`Z= 8 10^{-3} Ventura et al. MNRAS 424, 2345-2357. (2012) \n
        :math:`Z= 1.8 10^{-2} Dell’Agli et al. MNRAS 467, 4431-4440. (2017) \n
    
    """
    Z_star = np.array([0.0,3e-4,1e-3,8e-3,1.8e-2])
    m_star = [np.array([    1.5,     2.0,     2.5,3.0]),
              np.array([1.0,1.5,     2.0,     2.5]),
              np.array([    1.5,     2.0,     2.5,3.0]),
              np.array([    1.5,     2.0,     2.5,3.0]),
              np.array([    1.5,1.75,2.0,2.25,2.5,3.0])]
    m_dust = [np.array([    0.0,     0.0,     0.0,0.0]),
              np.array([1e-4,4e-4,6e-4,4.7e-4]),
              np.array([1.23e-7,2.84e-4,    7.56e-4,     1.77e-4]),
              np.array([        1.23e-7,    1.28e-4,    6.42e-4,9.06e-4]),
              np.array([        5.61e-5,2.82e-4,9.41e-4,2.53e-3,3.27e-3,5.09e-3])]
    
    return EjectaTable(Z_star, m_star, m_dust)

def silicon_carbide_dust_INAF():
    """ :math:`Z= 3 10^{-4}  Di Criscienzo et al. MNRAS. 433, 313-323.(2013)\n
        :math:`Z= 10^{-3}  Ventura et al. MNRAS. 420, 1442–1456. (2012) \n
        :math:`Z= 8 10^{-3} Ventura et al. MNRAS 424, 2345-2357. (2012) \n
        :math:`Z= 1.8 10^{-2} Dell’Agli et al. MNRAS 467, 4431-4440. (2017) \n
    
    """
    Z_star = np.array([3e-4, 1e-3, 8e-3, 1.8e-2])
    m_star = [np.array([1.5,       2.0,      2.5, 3.0]),
              np.array([1.5,       2.0,      2.5, 3.0]),
              np.array([1.5,       2.0,      2.5, 3.0]),
              np.array([1.5, 1.75, 2.0, 2.25,2.5, 3.0])]
    m_dust = [np.array([0.0,                   0.0,              0.0,  0.0]),
              np.array([3.85e-8,           3.55e-6,           1.08e-5, 2.60e-5]),
              np.array([3.85e-8,               0.0,           1.86e-4, 2.33e-4]),
              np.array([2.08e-4, 1.05e-4, 1.10e-4, 6.01e-4, 8.93e-4, 9.40e-4])]
    
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
