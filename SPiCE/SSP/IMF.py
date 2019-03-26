from SPiCE.Ingredients import Ingredient

#-------------------------------------------------------------------------------

class IMF(Ingredient):
    """
    Initial Mass Function.
    """
    
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
#            dummy = '_{}_init'.format(self.name)
##            if(dummy in dir(self)):
#        else:
#            print 'ERROR: IMF "{}" not defined'.format(self.name)
#            print dummy
#    
#    def phi(self, m):
#        """
#        Given the stellar mass m, in solar masses,
#        return the number of stars between m and m+dm per unit total mass,
#        \n dN/dm / int_0^\infty m dN/dm dm
#        \n in solar masses^-2
#        """
#        return shape(m)
#            
#    def shape(self, m):
#        print 'ERROR: IMF not defined'
#        
#    def _Kroupa_shape(self, m):
#        return m**-2.35
    
#-------------------------------------------------------------------------------

class Salpeter(IMF):
    """Salpeter (1955; ApJ 121, 161)"""
    
    def __init__(self, m_min=.1, m_max=100):
        print 'Salpeter constructor callled'
        self.m_min = m_min
        self.m_max = m_max
  
    def phi(self, m):
        if( m<self.m_min or m>self.m_max ):
            return 0
        return(m**-2.35)
      
#-------------------------------------------------------------------------------

class Kroupa(IMF):
    """Kroupa (2001; ...)"""
    
#    def __init__(self):
#        self.m_min = 0.1
#        self.m_max = 100
  
    def phi(self, m):
        print "NOT DEFINED YET!!!"
      
#-------------------------------------------------------------------------------

IMF_options = {}
IMF_options['Salpeter'] = Salpeter

#-------------------------------------------------------------------------------
class IMF_2():
    
    def __init__(self):
        
        self.imfs_dict = {}
        self.imfs_dict['sal'] = self.salpeter
        self.imfs_dict['kro'] = self.kroupa
        
    def phi_salpeter(self,a, b, c):
        self.a = 0
        self.b = 100
        self.c = 1
        return a+b+c
        
    def phi_kroupa(self):
       return 1
    
