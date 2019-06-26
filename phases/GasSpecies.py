'''
Ideal gas classes

Mario Romero        May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
import GasGenerics as gas


'''
SPECIFIC GASES
This script contains all realistic gas species (e.g. Hydrogen, Helium, etc). They are subclasses of classes from 'GasGenerics.py'
'''

#--------------
#MONOATOMIC SPECIES
#Required data = particle mass
#--------------
class Neutral_Hydrogen(gas.Monoatomic):

    _particle_mass = (1.008*cte.u).to(u.g) #1.008*atomic_mass

    def update_derivatives(self,term):
        print("Neutral_Hydrogen: Work in Progress...")

    def evolve(self,dt):
        print("Neutral_Hydrogen: 'evolve()' written for testing purposes!")
        self.state(P=self._pressure,T=self._temperature,M=self._gas_mass)


class Ionized_Hydrogen(gas.Monoatomic):

    _particle_mass = (cte.m_p).to(u.g) #Proton mass

    def update_derivatives(self,term):
        print("Ionized_Hydrogen: Work in Progress...")

    def evolve(self,dt):
        print("Ionized_Hydrogen: 'evolve()' written for testing purposes!")
        self.state(P=self._pressure,T=self._temperature,M=self._gas_mass)

#--------------
#DIATOMIC SPECIES
#Needed data: particle masses (array), distance between particles and their fundamental vibration mode.
#--------------
class Molecular_Hydrogen(gas.Diatomic):
    
    _atom_mass = [(1.008*cte.u).to(u.g) , (1.008*cte.u).to(u.g)] #Two hydrogen atoms
    _atom_distance = 74.14*1e-10 * u.cm #Taken from wikipedia
    _wavenumber = 4342.0*(1./u.cm) #wavenumber (k) of fundamental vibration. Taken from here: https://www.chem.purdue.edu/gchelp/vibs/h2.html  //
    
    
    def update_derivatives(self,term):
        print("Molecular_Hydrogen: Work in Progress...")
    
    def evolve(self,dt):
        print("Molecular_Hydrogen: 'evolve()' written for testing purposes!")
        self.state(P=self._pressure,T=self._temperature,M=self._gas_mass)
