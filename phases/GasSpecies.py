#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ideal gas classes

Mario Romero		May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
import GasGenerics as gas


'''
This script contains all realistic gas species (e.g. Hydrogen, Helium, etc). They are subclasses of classes from 'GasGenerics.py'

You only need to redefine here 'update_derivatives' and 'default_settings'
'''

class Neutral_Hydrogen(gas.Monoatomic):

	_particle_mass = (1.008*cte.u).to(u.g) #1.008*atomic_mass

	def __init__(self):
		print("Warning: code written for testing purposes!")
		self.default_settings()

	def default_settings(self):
		self._set()
		return{
			'current_mass':0.0*u.solMass,
			'dm_dt': 0.0*(u.solMass/u.yr),
		}

	def update_derivatives(self,term):
		#DISCLAIMER: THIS IS AN EXAMPLE!
		#print("Warning: code written for testing purposes!")
		uV = u.cm*u.cm*u.cm

		self.dm_dt = 0.0*u.solMass/u.yr
		dt = 0.0*u.yr
		for element in term:

			add = 0.0*u.solMass/u.yr

			#Recombination (There is ionized hydrogen)
			if (isinstance(element,Ionized_Hydrogen)):

				#ov = 4.1e-10*uV/u.s * (element._temperature/u.K)**(-0.8)
				#tau = 1./(ov * (element._number_density).to(1./uV))
				tau = 50.*u.yr

				add = (element._gas_mass).to(u.solMass) / (tau).to(u.yr)

			self.dm_dt += add

	def evolve(self,dt):

		#Now evolve (simple Euler scheme)
		self._gas_mass += self.dm_dt * (dt).to(u.yr)

		#And get the new state
		self._state(self._pressure,self._temperature,self._gas_mass,-1)


class Ionized_Hydrogen(gas.Monoatomic):

	_particle_mass = (cte.m_p).to(u.g) #Proton mass

	def __init__(self):
		print("Warning: code written for testing purposes!")
		self.default_settings()

	def default_settings(self):
		self._set()
		return{
			'current_mass':0.0*u.solMass,
			'dm_dt': 0.0*(u.solMass/u.yr),
		}

	def update_derivatives(self,term):
		#DISCLAIMER: THIS IS AN EXAMPLE!
		#print("Warning: code written for testing purposes!")

		uV = u.cm*u.cm*u.cm

		self.dm_dt = 0.0*u.solMass/u.yr
		dt = 0.0*u.yr


		for element in term:

			add = 0.0*u.solMass/u.yr

			#Recombination (There is neutral hydrogen)
			if (isinstance(element,Neutral_Hydrogen)):

				#ov = 4.1e-10*uV/u.s * (self._temperature/u.K)**(-0.8)
				#tau = 1./(ov * (self._number_density).to(1./uV))
				tau = 50.*u.yr

				add = - (self._gas_mass).to(u.solMass) / ((tau).to(u.yr))

			self.dm_dt += add

			#print(self.dm_dt)

	def evolve(self,dt):
		
		#Now evolve (simple Euler scheme)
		self._gas_mass += self.dm_dt * (dt).to(u.yr)

		#And get the new state
		self._state(self._pressure,self._temperature,self._gas_mass,-1)
