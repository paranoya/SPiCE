#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
An example

Mario Romero		June 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
import GasGenerics as gas
import GasSpecies as species

'''
Each species has its own class defined in 'GasSpecies.py'
'''

#(1) Let's declare auxiliary variables

uV = u.cm*u.cm*u.cm

M0_a = 0.*u.solMass
T0_a = 100.*u.K
P0 = ((1.e4*u.K/uV)*cte.k_B).to(u.erg/uV)

M0_i = 1000.*u.solMass
T0_i = 1000.*u.K

dt = 1.*u.yr

#(2) Let's declare hydrogen objects
HI = species.Neutral_Hydrogen()
HI.init(P=P0,T=T0_a,M=M0_a) #Your initial conditions goes here

HII = species.Ionized_Hydrogen()
HII.init(P=P0,T=T0_i,M=M0_i)

#(3) Now evolve

t = 0.*u.yr
tf = 1000.*u.yr


while(t < tf):
	print(t,HI.number_density(),HI.mass())
	print(t,HII.number_density(),HII.mass())
	print("\n")

	HI.update_derivatives([HI,HII])
	HII.update_derivatives([HI,HII])

	HI.evolve(dt)
	HII.evolve(dt)
	t += dt

	#break
