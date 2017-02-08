import sys

def add_to_path(path):
    if(path in sys.path):
        print path,'already there!'
    else:
        print path,'added'
        sys.path.append(path)

add_to_path('/home/yago/git/SPiCE/')


#-------------------------------------------------------------------------------

#import SPiCE as sp
#imf = sp.SSP.IMF.Salpeter()

from SPiCE.SSP import IMF as ii
#imf = Salpeter()

#imf = ii.IMF.create('Salpeter',())

#print imf.phi(10)

#-------------------------------------------------------------------------------

imf_object = ii.IMF_2()
my_imf = imf_object.imfs_dict['sal']
#my_imf = imf_object.imfs_dict['kro']

#-------------------------------------------------------------------------------

print my_imf(1,2,3)

print my_imf(1,2,3)

print my_imf(1,2,3)

#-------------------------------------------------------------------------------
