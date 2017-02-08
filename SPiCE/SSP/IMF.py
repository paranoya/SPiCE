from abc import ABCMeta, abstractmethod

#-------------------------------------------------------------------------------

class IMF:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def phi(m):
        pass
    
    def create(self,imf,args):
        if IMF_options.has_key(imf)(args):
            return IMF_options[imf]
        else:
            print 'Requested IMF not available:', imf
            
#-------------------------------------------------------------------------------

class Salpeter(IMF):
    
    def __init__(self, m_min=.1, m_max=100):
        self.m_min = m_min
        self.m_max = m_max
  
    def phi(self, m):
        if( m<self.m_min or m>self.m_max ):
            return 0
        return(m**-2.35)
      
#-------------------------------------------------------------------------------

class Kroupa(IMF):
    
    def __init__(self):
        self.m_min = 0.1
        self.m_max = 100
  
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
'''
'''        
        
        self.a = 0
        self.b = 100
        self.c =             
        return a+b+c
        
    def phi_kroupa(self):
       return 1
    
