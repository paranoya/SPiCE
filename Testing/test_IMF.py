import sys

def add_to_path(path):
    if(path in sys.path):
        print path,'already there!'
    else:
        print path,'added'
        sys.path.append(path)

add_to_path('/home/yago/git/SPiCE/')


#-------------------------------------------------------------------------------

#import SPiCE
#model = SPiCE.Model('SPiCE_parameters.txt')


#-------------------------------------------------------------------------------
