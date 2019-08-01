'''
Ideal gas classes

Mario Romero        May 2019
'''

import numpy as np
import astropy.units as u
import astropy.constants as cte
from . import basic

'''
PARENT CLASSES
classes defined here should not be defined as objects in the main code.
'''
class Gas(basic.Phase):

    #---------------------
    #DEFAULT SETTINGS
    #---------------------
    def __init__(self, model, params):
        #What everyone does
        self.model = model
        self.params = {**self.default_settings(), **params}
        self.mass_history_Msun = [float(self.params['initial_mass_Msun'])]
        self.temperature_history_K = [float(self.params['initial_temperature_K'])]
        self.pressure_history_cgs = [float(self.params['initial_pressure_cgs'])]
        
        #self._count = 0
        self._constants()
        self._set()
        self._state()
    
    def _constants(self):
        #Useful conversions and constants (this will save us LOTS of parentesis, trust me!)
        self._solMass_to_g = ((1*u.solMass).to(u.g)).value
        self._kB = ((cte.k_B).to(u.erg/u.K)).value #Boltzmann constant in erg/K
        self._hP = ((cte.h).to(u.erg*u.s)).value #Planck constant in erg*s
        self._hbar = self._hP/(2.*np.pi)
        self._c = ((cte.c).to(u.cm/u.s)).value #Speed of light
    
    def _set(self):
        #All internal variables will be in cgs
        
        self._temperature = self.temperature_history_K[-1]
        self._pressure = self.pressure_history_cgs[-1]
        self._gas_mass = self.mass_history_Msun[-1]*self._solMass_to_g
        #print(self.mass_history_Msun[-1],self._solMass_to_g,self.mass_history_Msun[-1]*self._solMass_to_g)
        #self._count +=1
        #if self._count > 2:
        #    raise
    
    def current_temperature_K(self):
        return self.temperature_history_K[-1]
    def current_pressure_cgs(self):
        return self.pressure_history_cgs[-1]
    
    def update_mass(self, timestep_Gyr):
        #Euler integrator is becoming a bottleneck, it should be replaced with a more efficient one.
        #Actually, this should be called 'update_all', but is called this way to keep compatibility
        #print(self.current_mass_Msun())
        self.mass_history_Msun.append(self.current_mass_Msun() + self.dm_dt_Msun_Gyr*timestep_Gyr)
        
        #If you don't want to store the pressure history because, for example, it does not change over time
        #   you only have to comment the relevant line of these two.
        self.temperature_history_K.append(self.current_temperature_K())
        self.pressure_history_cgs.append(self.current_pressure_cgs())
        
        self._set()
        self._state()

    def default_settings(self):
        return{
            'initial_mass_Msun':0.0,
            'initial_temperature_K': 0.0,
            'initial_pressure_cgs':0.0
        }

    #---------------------
    #COMMON ATRIBUTES/METHODS TO ALL DERIVED CLASSES
    #---------------------
    def _compute_variables_indepedent_of_state(self):

        try:
            self._number_density = self._number_particles / self._volume
            self._thermal_energy_density = self._thermal_energy / self._volume
            self._gamma = 1.+(self._pressure/self._thermal_energy_density)
        except (FloatingPointError,ZeroDivisionError):
            self._number_density = 0.0
            self._thermal_energy_density = 0.0
            self._gamma = np.Infinity
        self._mass_density = self._number_density * self._particle_mass_g
        self._chemical_potential = self._kB*self._temperature*np.log(self._fugacity)
        #print(self._thermal_energy_density , self._thermal_energy , self._volume)

    #---------------------
    #OUTPUTS
    #---------------------
    #def mass(...): comes from basic phase. So I do not redefine here
    def pressure(self,units=u.erg/(u.cm*u.cm*u.cm)):
        return ((self._pressure)*units).value
    def temperature(self,units=u.K):
        return ((self._temperature)*units).value
    def number_particles(self,units=u.m/u.m):
        return ((self._number_particles)*units).value
    def thermal_energy(self,units=u.erg):
        return ((self._thermal_energy)*units).value
    def fugacity(self,units=u.m/u.m):
        return ((self._fugacity)*units).value
    def volume(self,units=(u.cm*u.cm*u.cm)):
        return ((self._volume)*units).value
    def chemical_potential(self,units=u.erg):
        return (self._chemical_potential).to(units)
    def number_density(self,units=1./(u.cm*u.cm*u.cm)):
        return ((self._number_density)*units).value
    def mass_density(self,units=u.g/(u.cm*u.cm*u.cm)):
        return ((self._mass_density)*units).value
    def thermal_energy_density(self,units=u.erg/(u.cm*u.cm*u.cm)):
        return ((self._thermal_energy_density(self))*(units)).value
    def adiabatic_constant(self,units=u.m/u.m):
        return ((self._gamma)*units).value

    #---------------------
    #POLYMORPHIC METHODS
    #---------------------
    #I.e.: These are the ONLY functions you have to redefine in each subclass
    def _state(self,P=-1,T=-1,M=-1,N=-1):#inputs: pressure, temperature, number of particles, thermal energy, mass
        #print("Warning: Using a parent class. Should not happen!")
        raise NameError("Called by parent class. Should not happen!")

    #---------------------
    #DEBUGGING
    #---------------------
    def debug(self):
        print([self._gas_mass,self._particle_mass_g])

'''
CHILDS OF GAS
These classes must have 'state()' well defined and not polymorphic
'''
class Monoatomic(Gas):
    
    #---------------------
    #STATE METHOD
    #---------------------
    def _state(self):#inputs: pressure, temperature, number of particles, thermal energy, mass
        #Here we compute the other thermodynamic variables
        
        self._number_particles = (self._gas_mass)/(self._particle_mass_g)
        self._thermal_energy = 1.5*self._number_particles * self._kB * self._temperature
        self._volume = (2.*self._thermal_energy) / (3.*self._pressure)

        #Fugacity = exp(chemical_potential / kT) . It is another way to describe the chemical potential
        self._fugacity = self._pressure * (2.*np.pi*self._particle_mass_g / (self._hP*self._hP) )**(-1.5) * (self._kB*self._temperature)**(-2.5)
        #Compute the other variables
        self._compute_variables_indepedent_of_state()

class Diatomic(Gas):
    
    #---------------------
    #AUXILIARY METHODS
    #---------------------
    def _molecule_mass(self):
        return self._atom_mass_g[0]+self._atom_mass_g[1] #ESTOY AQUÍ
    
    def _moment_of_inertia(self):
        #Get reduced mass
        m_r = self._atom_mass_g[0]*self._atom_mass_g[1] / (self._atom_mass_g[0]+self._atom_mass_g[1]) 
        return m_r*self._atom_distance_cm*self._atom_distance_cm
    
    def _angular_frequency(self):
        return self._wavenumber_cm_minus1 * self._c 
    
    #---------------------
    #PARTITION FUNCTION METHODS
    #---------------------
    def _Z_rot(self):
        #We compute Z for only rotations

        #Compute a parameter to check if quantum effects are important
        theta =  0.5 * self._hbar*self._hbar / (self._kB * self._temperature * self._moment_of_inertia()) 
        #Now do stuff
        Z = None
        dZ_db = None #Partial derivative of Z with respect to beta = 1./kT (units: erg)
        if theta <= 1: #All rotational modes are enabled (=classical)
            Z = 1./theta
            dZ_db = - self._kB * self._temperature / theta
        else: #All rotational modes are disabled
            Z = 1.0
            dZ_db = 0.0
        
        return [Z , dZ_db]
        '''
        Note that this is a simplification.
        The exact method has Z = sum (2l+1)*exp(-theta*l(l+1)) ; for l=0 to infinity. 
        Be aware that it's computationally expensive.
        '''
    
    def _Z_vib(self):
        #We compute Z for only molecule vibrations
        
        #no_units = u.cm/u.cm
        #Compute a parameter to check if quantum effects are important
        xi = self._hbar * self._angular_frequency() / (self._kB * self._temperature)     
        #Now do stuff
        Z = None
        dZ_db = None #Partial derivative of Z with respect to beta = 1./kT (units: erg)
        if xi > 1: #All vibrational modes are disabled
            Z = 1.0
            dZ_db = 0.0
        else:
            Z = 1./xi
            dZ_db = - self._kB * self._temperature / xi
        
        return [Z , dZ_db]
        '''
        Again, this is a simplification.
        The exact method has Z = sum exp(-n*xi) = 1./(1-exp(-xi)) . 
        Also note that the zero of energies is set as all vibrations at the fundamental state of the harmonic oscillator.
        '''
        
    #---------------------
    #STATE METHOD
    #---------------------
    def _state(self):#inputs: pressure, temperature, number of particles, mass

       #uV = (u.cm*u.cm*u.cm) #volume units
        #no_units = u.m/u.m #dimensionless units
        
        #Because you give each atom mass individually, you need to construct the particle mass first.
        self._particle_mass_g = self._molecule_mass()
        #Get the total number of particles
        self._number_particles = (self._gas_mass)/(self._particle_mass_g)
        #Let's define an useful variable
        NkT = self._number_particles * (self._kB) * self._temperature
        
        #Partition functions (they are arrays, [0] is the Z itself, and [1] the derivative with respect to beta)
        Zrot = self._Z_rot()
        Zvib = self._Z_vib()
        
        #Now we compute the remaining variables
        self._volume =  NkT / self._pressure 
        #Fugacity = exp(chemical_potential / kT) . It is another way to describe the chemical potential
        self._fugacity = self._pressure * (2.*np.pi*self._particle_mass_g / (self._hP*self._hP) )**(-1.5) * (self._kB*self._temperature)**(-2.5) / (Zrot[0]*Zvib[0])
        #Thermal energy
        #const_factor = 1.5 - (Zrot[1]/( Zrot[0] * self._kB * self._temperature )) - (Zvib[1]/( Zvib[0] * self._kB * self._temperature ))
        const_factor = 1.5                                                      #Translational part
        const_factor -= (Zrot[1]/( Zrot[0] * self._kB * self._temperature ))    #Rotational part
        const_factor -= (Zvib[1]/( Zvib[0] * self._kB * self._temperature ))    #Vibrational part
        self._thermal_energy = NkT * const_factor
        
        self._compute_variables_indepedent_of_state()
