#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ideal gas classes

Mario Romero		May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte


'''
PARENT CLASS
'''
class Gas(MultiphaseMedium):
#class Gas(object):

	#---------------------
	#DEFAULT SETTINGS
	#---------------------

	def default_settings(self):
		self._set()
		return{
			'current_mass':0.0*u.solMass,
			'dm_dt': 0.0*(u.solMass/u.yr),

			'particle_mass':0.0*u.g,
		}

	#---------------------
	#COMMON ATRIBUTES/METHODS TO ALL DERIVED CLASSES
	#---------------------
	def _set(self):

		uV = (u.cm*u.cm*u.cm) #volume units
		no_units = u.m/u.m    #dimensionless units
		#Internal variables
		self._pressure = 0.0*(u.erg/u.s)
		self._temperature = 0.0*u.K
		self._number_particles = 0.0*no_units
		self._thermal_energy = 0.0*u.erg
		self._fugacity = 0.0*no_units
		self._volume = 0.0*uV
		self._gas_mass = 0.0*u.solMass
		self._chemical_potential = 0.0*u.erg
		self._number_density = 0.0 / uV
		self._mass_density = 0.0*u.g/ uV
		self._thermal_energy_density = 0.0*u.erg/uV
		self._gamma = 0.0*no_units
	
	def _compute_variables_indepedent_of_state(self):
		uV = (u.cm*u.cm*u.cm) #volume units
		no_units = u.m/u.m    #dimensionless units

		self._gas_mass = (self._number_particles * self._particle_mass).to(u.solMass)
		self._number_density = (self._number_particles / self._volume).to(1./uV)
		self._mass_density = (self._number_density * self._particle_mass).to(u.g/uV)
		self._thermal_energy_density = (self._thermal_energy / self._volume).to(u.erg/uV)
		self._chemical_potential = (cte.k_B*self._temperature*np.log(self._fugacity)).to(u.erg)
		self._gamma = (1.+(self._pressure/self._thermal_energy_density)).to(no_units)

	#---------------------
	#CONSTRUCTORS
	#---------------------
	#Update
	def init(self,P=-1,T=-1,M=-1,N=-1):
		self._state(P,T,M,N)

	#---------------------
	#OUTPUTS
	#---------------------
	def mass(self,units=u.solMass): #Polymorph from Multiphase
		return (self._gas_mass).to(units)	
	def pressure(self,units=u.erg/(u.cm*u.cm*u.cm)):
		return (self._pressure).to(units)
	def temperature(self,units=u.K):
		return (self._temperature).to(units)
	def number_particles(self,units=u.m/u.m):
		return (self._number_particles).to(units)
	def thermal_energy(self,units=u.erg):
		return (self._thermal_energy).to(units)
	def fugacity(self,units=u.m/u.m):
		return (self._fugacity).to(units)
	def volume(self,units=(u.cm*u.cm*u.cm)):
		return (self._volume).to(uV)
	def chemical_potential(self,units=u.erg):
		return (self._chemical_potential).to(units)
	def number_density(self,units=1./(u.cm*u.cm*u.cm)):
		return (self._number_density).to(units)
	def mass_density(self,units=u.g/(u.cm*u.cm*u.cm)):
		return (self._mass_density).to(units)
	def thermal_energy_density(self,units=u.erg/(u.cm*u.cm*u.cm)):
		return (self._thermal_energy_density(self)).to(units)
	def adiabatic_constant(self,units=u.m/u.m):
		return (self._gamma).to(units)

	#---------------------
	#POLYMORPHIC METHODS
	#---------------------
	#I.e.: These are the ONLY functions you have to redefine in each subclass
	def _state(self,P,T,M,N):#inputs: pressure, temperature, number of particles, thermal energy, mass
		raise NameError("Called by parent class. Should not happen!")

	def update_derivatives(self,term):
		raise NameError("Called by parent class. Should not happen!")

'''
CHILD CLASS
'''
#These classes must have '_state()' well defined and not polymorphic
#You can call this class as a generic monoatomic gas instead of a particular species, but you have to define the mass of its particles.
class Monoatomic(Gas):
	
	def default_settings(self):
		self._set()
		return{
			'current_mass':0.0*u.solMass,
			'dm_dt': 0.0*(u.solMass/u.yr),

			'particle_mass':0.0*u.g,
		}

	def _state(self,P,T,M,N):#inputs: pressure, temperature, number of particles, thermal energy, mass
		uV = (u.cm*u.cm*u.cm) #volume units
		no_units = u.m/u.m    #dimensionless units

		#Convert mass, if given
		if M != -1:
			N = (M.to(u.g))/(self._particle_mass).to(u.g)

		#You MUST give pressure and number of particles (or total mass)
		if (P == -1) or (N == -1):
			raise NameError("Gas._state() bad initialized! You must give pressure and total mass/number or particles!")
		else:
			#Initialize thermodynamic variables
			self._pressure = P.to(u.erg/uV)
			self._number_particles = N.to(no_units)

		#If temperature is given. I will follow a different path
		if T != -1:
			self._temperature = T.to(u.K)

			#We compute energy first
			self._thermal_energy = (1.5*self._number_particles * (cte.k_B) * self._temperature).to(u.erg)

			#Volume...
			self._volume = ((2.*self._thermal_energy) / (3.*self._pressure)).to(uV)

			#And fugacity
			self._fugacity = (self._pressure * (2.*np.pi*self._particle_mass / (cte.h*cte.h) )**(-1.5) * (cte.k_B*self._temperature)**(-2.5)).to(no_units)

		else:
			raise NameError("Gas.state bad initialized! You must give either temperature or internal energy")
	
		#Compute the other variables
		self._compute_variables_indepedent_of_state()

	#---------------------
	#(STILL) POLYMORPHIC METHODS
	#---------------------
	#Note that, this time, the method is well defined here as well
	def update_derivatives(self,term):
		raise NameError("Work in Progress...")
