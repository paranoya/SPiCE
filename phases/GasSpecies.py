'''
Ideal gas classes

Mario Romero        May 2019
'''

#import numpy as np
import astropy.units as u
import astropy.constants as cte
from . import GasGenerics as gas

'''
SOME CONSTANTS
'''

atomic_mass_g = ((cte.u).to(u.g)).value
proton_mass_g = ((cte.m_p).to(u.g)).value

'''
SPECIFIC GASES
This script contains all realistic gas species (e.g. Hydrogen, Helium, etc). They are subclasses of classes from 'GasGenerics.py'
'''

#--------------
#MONOATOMIC SPECIES
#Required data = particle mass
#--------------
class Neutral_Hydrogen(gas.Monoatomic):
    _particle_mass_g = 1.008*atomic_mass_g 

class Ionized_Hydrogen(gas.Monoatomic):
    _particle_mass_g = proton_mass_g #Proton mass

#--------------
#DIATOMIC SPECIES
#Needed data: particle masses (array), distance between particles and their fundamental vibration mode.
#--------------
class Molecular_Hydrogen(gas.Diatomic):
    _atom_mass_g = [1.008*atomic_mass_g , 1.008*atomic_mass_g ] #Two hydrogen atoms
    _atom_distance_cm = 74.14*1e-10  #Taken from wikipedia
    _wavenumber_cm_minus1 = 4342.0 #wavenumber (k) of fundamental vibration. Taken from here: https://www.chem.purdue.edu/gchelp/vibs/h2.html  //
