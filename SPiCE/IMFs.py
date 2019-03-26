from Ingredients import Ingredient, FloatNumber

#-------------------------------------------------------------------------------

class IMF(Ingredient):
    """
    Initial Mass Function.
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

    def __init__(self, parameters):
        super(self.__class__,self).__init__(parameters)
        self._setup()
        self._normalize()
        
    def _normalize(self):
        """**TO DO**: Normalize IMF so that :math:`\\int_0^\\infty m\\,\\phi(m)\\,dm = 1`"""
        self.norm = 1
        
    def phi(self, m):
        """
        Given the stellar mass :math:`m`, in solar masses,
        return the number of stars between :math:`m` and :math:`m+dm` per unit total mass,
        \n :math:`\\phi(m) = \\frac{ \\frac{dN}{dm}(m) }{ \\int_0^\infty m \\frac{dN}{dm}(m)\\ dm }`
        \n in :math:`M_\\odot^{-2}.`
        """
        if( m<self.m_min or m>self.m_max ):
            return 0
        return self_norm * self._shape(m)
    
#    Functions to be overriden by IMF subclasses:
    
    def _setup(self):
        """Initialization, called once upon construction."""
        pass
    
    def _shape(self, m):
        """Unnormalized shape of the IMF, called every time phi(m) is evaluated."""
        print 'ERROR: IMF not defined'
        
#-------------------------------------------------------------------------------

class Salpeter_m_min(FloatNumber):
    """Minimum mass of a star, in Msun"""
    minimum_allowed = 0.001
    maximum_allowed = 1.0
    default_value = 0.1

class Salpeter_m_max(FloatNumber):
    """Maximum mass of a star, in Msun"""
    minimum_allowed = 1.0
    maximum_allowed = 1000
    default_value = 100

class Salpeter(IMF):
    """Salpeter (1955; ApJ 121, 161)"""
    contains_ingredient_classes = [Salpeter_m_min, Salpeter_m_max]
    
    def _setup(self):
        self.m_min = self.ingredients['Salpeter_m_min'].value
        self.m_max = self.ingredients['Salpeter_m_max'].value
  
    def _shape(self, m):
        if( m < self.m_min ):
            return 0
        elif( m < self.m_max ):
            return( m**-2.35 )
        else:
            return 0

#-------------------------------------------------------------------------------

class Kroupa(IMF):
    """**TO DO**: check Kroupa (2001; ...)"""
    
    def _setup(self):
        self.m_min = .01
        self.m_max = 100
        
    def _shape(self, m):
        if( m < self.m_min ):
            return 0
        elif( m < 0.08 ):
            return( m**-0.3 )
        elif( m < 0.5 ):
            return( m**-1.3 )
        elif( m < self.m_max ):
            return( m**-2.3 )
        else:
            return 0
      
#-------------------------------------------------------------------------------
