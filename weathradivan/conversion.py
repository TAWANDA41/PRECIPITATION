


# FUNCTIONS::
# dBZ2Z - Convert from dBZ to linear Z units
# Z2dBZ - Convert from linear Z units to dBZ
# si2kmh - Convert from SI wind units to km/hr
# si2mph - Convert from SI wind units to miles per hour
# si2kts - Convert from SI wind units to knots
#-------------------------------------------------------------------
# Load the needed packages
import numpy as np
###################
# DEFINE CONTSTANTS
###################

###################
# BEGIN FUNCTIONS
###################

def dBZ2Z(dBZ):
    

    Zlin = 10.**(dBZ/10.)

    return Zlin
    
#============

def Z2dBZ(Zlin):
  
    dBZ = 10. * np.log10(Zlin)

    return dBZ
    
#=============

def si2kmh(SI):
   
    kmh = SI * 3600. / 1000.
    
    return kmh
    
#=============

def si2mph(SI):
   
    mph = SI * 0.62137 / 1000. * 3600.
    
    return mph
    
#=============

def si2kts(SI):
  

    kts = SI * 0.51
    
    return kts
    
#=============

def kmh2si(kmh):
   
    SI = mph * 1000. / (0.62137 * 3600.)
    
    return SI
    
#============

def kts2si(kts):
    
 


