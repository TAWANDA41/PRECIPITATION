

# FUNCTIONS::
# r_effective - Effective radius
# half_power_radius - Half-power beam radius
# ray_height - Height of a ray
# sample_vol_ideal - Ideal Sample volume
# sample_vol_gauss - Sample volume from Gaussian-distributed beam
# range_correct - Range distance corrected for elevation angle "loss" along ground
# beam_block_frac - Partial Beam blockage fraction 
#-------------------------------------------------------------------
# Load the needed packages
import numpy as np

###################
# DEFINE CONTSTANTS
###################
SLP = 1013.25 # Sea-level Pressure [hPa]
P0 = 1000.  # Reference pressure [hPa]
c = 3e8 # Speed of light [m/s]
Re = 6371000 # Earth's average radius [m] assuming sphericity 
R43 = Re*4./3. # 4/3 Approximation effective radius for standard atmosphere [m]
kBoltz = 1.381e-23 # Boltzmann's constant [ m^2 kg s^-2 K^-1]

# Earth radius taken according to International Union of Geodesy and Geophysics
###################
# BEGIN FUNCTIONS
###################

def r_effective(dNdH=-39e-6):
    

    # Convert earth's radius to km for common dN/dH values and then
    # multiply by 1000 to return radius in meters
    R1 = (1. / ((1/(Re/1000.)) + (dNdH))) * 1000.

    return R1
    
#=============

def half_power_radius(r, bwhalf):
   

    # Convert earth's radius to km for common dN/dH values and then
    # multiply by 1000 to return radius in meters
    Rhalf = (r * np.deg2rad(bwhalf)) / 2.

    return Rhalf
    
#===============

def ray_height(r, elev, H0, R1=R43):
    
    # Convert earth's radius to km for common dN/dH values and then
    # multiply by 1000 to return radius in meters
    Term1 = np.sqrt(r**2 +R1**2 + 2*r*R1*np.sin(np.deg2rad(elev)))
    H = Term1 - R1 + H0

    return H
    
#============

def sample_vol_ideal(r, bwH, bwV, pLength):
    
    SVol = np.pi * (r * np.deg2rad(bwH)/2.) * (r * np.deg2rad(bwV)/2.) * (pLength/2.)
    return SVol
    
#===============

def sample_vol_gauss(r, bwH, bwV, pLength):
    

    Numer = np.pi * r**2 * np.deg2rad(bwH) * np.deg2rad(bwV) * pLength
    Denom = 16. * np.log(2)
    
    SVol = Numer / Denom
    return SVol
    
#===============

def range_correct(r, h, E):
    
    
    INPUT::
    -----
    r  : float
        Distance to sample volume from radar [m]
    h : float
        Height of the center of radar volume [m]
    E : float
        Elevation angle [deg]
    
    OUTPUT::
    -----
    rnew : float
        Adjusted range to sample volume [m]
    
    USAGE::
    -----
  rnew = range_correct(r,h,E)
    
    NOTES::
    -----
    This function requires that an array be passed!  If you need just one 
       point create a 2 element array with a begin point.
    This is now set up to only accept a 1D array I believe.  May need to 
       fix this in the future.
    

def beam_block_frac(Th, Bh, a):
   

    # First find the difference between the terrain and height of
    # radar beam (Bech et al. (2003), Fig.3)
    y = Th - Bh

    Numer = (y * np.sqrt(a**2 - y**2)) + (a**2 * np.arcsin(y/a)) + (np.pi * a**2 /2.)

    Denom = np.pi * a**2
    
    PBB = Numer / Denom

    return PBB
    
#==============

