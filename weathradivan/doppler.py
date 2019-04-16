
# NOTES::
#   Arrays seem to be able to be passed, but make sure they are float arrays
#    (e.g. created with numpy) and not lists
#
# FUNCTIONS::
# freq - Frequency
# wavelength - Wavelength
# pulse_length - Pulse Length
# pulse_duration - Pulse Duration
# fmax - Maximum frequency
# Vmax - Nyquist or maximum unambiguous velocity
# Rmax - Maximum unambiguous range
# Dop_dilemma - The "Doppler dilemma" either Nyq vel or Rmax yields the other
# Vshift - Shift in Doppler velocity due to moving platform
# Vmax_dual - Maximum unambiguous velocity from dual PRF system
#-------------------------------------------------------------------
# Load the needed packages
import numpy as np
###################
# DEFINE CONTSTANTS
###################
SLP = 1013.25 # Sea-level Pressure [hPa]
P0 = 1000.  # Reference pressure [hPa]
c = 3e8 # Speed of light [m/s]
Re = 6374000 # Earth's radius [m]
R43 = Re*4./3. # 4/3 Approximation effective radius for standard atmosphere [m]
kBoltz = 1.381e-23 # Boltzmann's constant [ m^2 kg s^-2 K^-1]

###################
# BEGIN FUNCTIONS
###################
def freq(lam):
    
    
    freq = c / lam

    return freq
    
#==============

def wavelength(freq):
   
    lam = c / freq

    return lam
    
#==============

def pulse_duration(tau):
    
    pDur = 2 * tau / c

    return pDur
    
#===============

def pulse_length(pDur):
    

    tau = c * pDur / 2

    return tau
    
#=============

def fmax(PRF):
   

    fmax = PRF/2.

    return fmax
    
#===============

def Vmax(PRF, lam):
   
    Vmax = PRF * lam / 4.

    return Vmax
    
#===============

def Rmax(PRF):
   
    Rmax = c / (2. * PRF)

    return Rmax
    


def Dop_dilemma(In, lam):
   

    Out = (c * lam / 8.) / In

    return Out
    


def Vshift(GS, psi):
  

    Vshift = GS * np.cos(np.deg2rad(psi))

    return Vshift
    
#=================

def Vmax_dual(lam, PRF1, PRF2):
    
