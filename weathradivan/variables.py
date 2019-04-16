

# FUNCTIONS::
# reflectivity - Radar reflectivity
# dop_vel - Doppler velocity
# CDR - Circular depolarization ratio
# LDR - Linear depolarization ratio
# ZDR - Differential reflectivity
# ZDP - Reflectivity difference
#-------------------------------------------------------------------
# Load the needed packages
import numpy as np
#===============================================================
# DEFINE CONTSTANTS
#===============================================================
#
#===============================================================
# BEGIN FUNCTIONS
#===============================================================
def reflectivity(Pt, G, Tau, lam, bwH, bwV, Lm, Lr, Pr, r, K=0.93):
    

    # Call the radar constant function
    C1 = radar_constant(Pt, G, Tau, lam, bwH, bwV, Lm, Lr)

    # 
    Ze = Pr * r**2 / (C1 * K**2)

    return Ze
    
#============

def rad_vel(f,lam):
    

    Vr = f * lam / 2.

    return Vr
    
#=============

def CDR(Zpar, Zorth):
    

    CDR = 10.* np.log10(Zpar/Zorth)

    return CDR
    
#===============

def LDR(Zh, Zv):
   

    LDR = 10. * np.log10(Zh / Zv)

    return LDR
    
#==============

def ZDR(Zh, Zv):
    
    ZDR = 10. * np.log10(Zh / Zv)

    return ZDR
    
#==============

def ZDP(Zh, Zv):
    

    if Zh > Zv:
        ZDP = 10.* np.log10(Zh - Zv)
    else:
        print ("Zh < Zv !")
        ZDP = np.nan
    return ZDP
    
#==============

def HDR(dBZh, ZDR):
    

    # Set the f(Zdr) based upon observations
    if ZDR <= 0:
        f = 27.
    elif ZDR > 0 and ZDR <= 1.74:
        f = 19. * ZDR + 27.
    elif ZDR > 1.74:
        f = 60.

    # Calculate HDR
    HDR = dBZh - f

    return HDR
    
#==============

