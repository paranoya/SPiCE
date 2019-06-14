'''
Ideal gas classes

Mario Romero        May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
import basic

'''
PARENT CLASSES
classes defined here should not be defined as objects in the main code.
'''
class Gas(basic.MultiphaseMedium):
#class Gas(object):

    #---------------------
    #DEFAULT SETTINGS
    #---------------------
    def default_settings(self):
        self._set()
        return{
            'current_mass':0.0*u.solMass,
            'dm_dt': 0.0*(u.solMass/u.yr),
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
    def __init__(self):
        print("Warning: '__init__()' code written for testing purposes!")
        self.default_settings()

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
        return (self._volume).to(units)
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
    def state(self,P=-1,T=-1,M=-1,N=-1):#inputs: pressure, temperature, number of particles, thermal energy, mass
        raise NameError("Called by parent class. Should not happen!")

    def update_derivatives(self,term):
        raise NameError("Called by parent class. Should not happen!")

'''
CHILDS OF GAS
These classes must have 'state()' well defined and not polymorphic
'''
class Monoatomic(Gas):
    
    #---------------------
    #STATE METHOD
    #---------------------
    def state(self,P=-1,T=-1,M=-1,N=-1):#inputs: pressure, temperature, number of particles, thermal energy, mass
        uV = (u.cm*u.cm*u.cm) #volume units
        no_units = u.m/u.m    #dimensionless units

        #Convert mass, if given
        if M != -1:
            N = (M.to(u.g))/(self._particle_mass).to(u.g)

        #You MUST give pressure, temperature and number of particles (or total mass)
        if (P == -1) or (T == -1) or (N == -1):
            raise NameError("Gas._state() bad initialized! You must give pressure, temperature and total mass/number or particles!")
        else:
            #Initialize thermodynamic variables
            self._pressure = P.to(u.erg/uV)
            self._number_particles = N.to(no_units)

            self._temperature = T.to(u.K)

            #We compute energy first
            self._thermal_energy = (1.5*self._number_particles * (cte.k_B) * self._temperature).to(u.erg)

            #Volume...
            self._volume = ((2.*self._thermal_energy) / (3.*self._pressure)).to(uV)

            #And fugacity
            self._fugacity = (self._pressure * (2.*np.pi*self._particle_mass / (cte.h*cte.h) )**(-1.5) * (cte.k_B*self._temperature)**(-2.5)).to(no_units)
    
        #Compute the other variables
        self._compute_variables_indepedent_of_state()

class Diatomic(Gas):
    
    #---------------------
    #AUXILIARY METHODS
    #---------------------
    def _molecule_mass(self):
        return (self._atom_mass[0]+self._atom_mass[1]).to(u.g)
    
    def _moment_of_inertia(self):
        #Get reduced mass
        
        m_r = ( self._atom_mass[0]*self._atom_mass[1] / (self._atom_mass[0]+self._atom_mass[1]) ).to(u.g)
        return m_r*self._atom_distance*self._atom_distance
    
    def _angular_frequency(self):
        return (self._wavenumber * cte.c ).to(1./u.s)
    
    #---------------------
    #PARTITION FUNCTION METHODS
    #---------------------
    def _Z_rot(self):
        
        no_units = u.cm/u.cm
        #Compute a parameter to check if quantum effects are important
        theta = ( 0.5 * cte.hbar*cte.hbar / (cte.k_B * self._temperature * self._moment_of_inertia()) ).to(no_units)
        
        #Now do stuff
        Z = None
        dZ_db = None #Partial derivative of Z with respect to beta = 1./kT
        if theta <= 1: #All rotational modes are enabled (=classical)
            Z = 1./theta
            dZ_db = - cte.k_B * self._temperature / theta
        else: #All rotational modes are disabled
            Z = 1.0*no_units
            dZ_db = 0.0*u.erg
        
        return [Z , dZ_db]
        '''
        Note that this is a simplification.
        The exact method has Z = sum (2l+1)*exp(-theta*l(l+1)) ; for l=0 to infinity. 
        Be aware that it's computationally expensive.
        '''
    
    def _Z_vib(self):
        
        no_units = u.cm/u.cm
        #Compute a parameter to check if quantum effects are important
        xi = ( cte.hbar * self._angular_frequency() / (cte.k_B * self._temperature) ).to(no_units)
        
        #Now do stuff
        Z = None
        dZ_db = None #Partial derivative of Z with respect to beta = 1./kT
        if xi > 1: #All vibrational modes are disabled
            Z = 1.0*no_units
            dZ_db = 0.0*u.erg
        else:
            Z = 1./xi
            dZ_db = - cte.k_B * self._temperature / xi
        
        return [Z , dZ_db]
        '''
        Again, this is a simplification.
        The exact method has Z = sum exp(-n*xi) = 1./(1-exp(-xi)) . 
        Note that the zero of energies is set as all vibrations at the fundamental state of the harmonic oscillator.
        '''
        
    #---------------------
    #STATE METHOD
    #---------------------
    def state(self,P=-1,T=-1,M=-1,N=-1):#inputs: pressure, temperature, number of particles, thermal energy, mass

        uV = (u.cm*u.cm*u.cm) #volume units
        no_units = u.m/u.m #dimensionless units
        
        #Because you give each atom mass individually, you need to construct the particle mass first.
        self._particle_mass = self._molecule_mass()
        
        #Convert mass, if given
        if M != -1:
            N = (M.to(u.g))/(self._particle_mass).to(u.g)
        
        #You MUST give pressure, temperature and number of particles (or total mass)
        if (P == -1) or (T == -1) or (N == -1):
            raise NameError("Gas._state() bad initialized! You must give pressure, temperature and total mass/number or particles!")
        else:
            #Initialize thermodynamic variables
            self._pressure = P.to(u.erg/uV)
            self._number_particles = N.to(no_units)
            self._temperature = T.to(u.K)
            
            #Useful variable
            NkT = (self._number_particles * (cte.k_B).to(u.erg/u.K) * self._temperature).to(u.erg)
            
            #Partition functions (they are arrays, [0] is the Z itself, and [1] the derivative with respect to beta)
            Zrot = self._Z_rot()
            Zvib = self._Z_vib()
            
            #We compute volume first (it's the ideal gas relation)
            self._volume = ( NkT / self._pressure ).to(uV)
            
            #Fugacity...
            self._fugacity = (self._pressure * (2.*np.pi*self._particle_mass / (cte.h*cte.h) )**(-1.5) * (cte.k_B*self._temperature)**(-2.5) / (Zrot[0]*Zvib[0]) ).to(no_units)
            
            #Thermal energy...
            const_factor = 1.5 - (Zrot[1]/( Zrot[0] * cte.k_B * self._temperature )).to(no_units) - (Zvib[1]/( Zvib[0] * cte.k_B * self._temperature )).to(no_units)
            self._thermal_energy = NkT * const_factor
            
            
        #Compute the other variables
        self._compute_variables_indepedent_of_state()