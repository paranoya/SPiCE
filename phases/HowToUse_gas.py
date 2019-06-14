#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
How to use the gas species

Mario Romero        June 2019
'''

import astropy.units as u
import astropy.constants as cte
import GasSpecies as species

'''
Each species has its own class defined in 'GasSpecies.py'
'''

#(1) Let's declare auxiliary variables

uV = u.cm*u.cm*u.cm #units
P0 = ((1.e4*u.K/uV)*cte.k_B).to(u.erg/uV) #Common pressure to all phases


#(2) Let's declare the initial conditions of hydrogen
#molecular phase
M0_m = 10.*u.solMass
T0_m = 10.*u.K

#atomic phase
M0_a = 100.*u.solMass
T0_a = 100.*u.K

#ionized phase
M0_i = 1000.*u.solMass
T0_i = 1000.*u.K

#(3) Let's declare hydrogen objects
H2 = species.Molecular_Hydrogen()
H2.state(P=P0,T=T0_m,M=M0_m) #Your initial conditions goes here

HI = species.Neutral_Hydrogen()
HI.state(P=P0,T=T0_a,M=M0_a)

HII = species.Ionized_Hydrogen()
HII.state(P=P0,T=T0_i,M=M0_i)

#(4) Do stuff (I'm throwing arbitrary numbers)
dt = 1.0*u.yr
t = 0.0*u.yr
tf = 0.5*u.yr

while(t < tf):

    #Get the derivatives
    H2.update_derivatives([H2,HI,HII])
    HI.update_derivatives([H2,HI,HII])
    HII.update_derivatives([H2,HI,HII])

    #Use your favourite integrator
    H2.evolve(dt)
    HI.evolve(dt)
    HII.evolve(dt)
    
    t += dt
