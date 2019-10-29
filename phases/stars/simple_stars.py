
import ../basic 
from scipy.integrate import trapz



class SimpleStars(basic.Phase):
    
    def __init__(self):
        self.products = {'sfr': [], 
                    'Z': []}
    
    def updateSFH(self, sfr):
        if True:
            self.products['sfr'].append(sfr)