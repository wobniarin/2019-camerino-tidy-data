"""
Code by Jake Vanderplas, Zeljko Ivezic, Andrew Connolly.

Submitted to John Hunter Excellence in Plotting contest 2013, won 3rd place.

Updated by Juan Nunez-Iglesias in June 2017 to use more modern MPL API.

Caption
-------
These panels visualize a 4-dimensional correlation between orbits and surface
color for about 35,000 main-belt asteroids (found between Mars and Jupiter)
observed by the Sloan Digital Sky Survey. The left panel quantifies the
variation of the asteroid surface chemistry using two measured colors: a* is an
optical color (as would be seen by e.g. human eyes) and i-z is a near-infrared
color (as would be seen by e.g. snake eyes). The dots corresponding to
individual objects are color-coded according to the object’s position in this
diagram. Blue shades are representative of carbonaceous surfaces, and orange
and green shades correspond to silicate surfaces. The right panel is
constructed with two orbital parameters: semi-major axis a (AU stands for
astronomical unit, equal to Sun-Earth distance) and sine of the orbital
inclination i. The vertical dashed lines mark the so-called Kirkwood gaps,
where no objects are found because of resonant gravitational scattering due to
Jupiter. These gaps define the three main-belt zones. The easily discernible
clusters of points correspond to the so-called orbital families of asteroids,
believed to be smaller remnants of larger objects destroyed in collisions. The
dots corresponding to individual objects are color-coded according to the
two-dimensional color palette from the left panel and the measured surface
colors. The vividly demonstrated fact that orbitally related asteroids also
have similar colors (and therefore similar surface chemistry) is evidence that
asteroids in these families share a common origin.

Source
------
http://conference.scipy.org/jhepc2013/2013/entry3/index.html
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from astroML.datasets import fetch_moving_objects
from astroML.plotting.tools import devectorize_axes


def compute_color(mag_a, mag_i, mag_z, a_crit=-0.1):
    """
    Compute the scatter-plot color using code adapted from
    TCL source used in Parker 2008.
    """
    # define the base color scalings
    red = np.ones_like(mag_i)
    green = 0.5 * 10 ** (-2 * (mag_i - mag_z - 0.01))
    blue = 1.5 * 10 ** (-8 * (mag_a + 0.0))

    # enhance green beyond the a_crit cutoff
    green += 10. / (1 + np.exp((mag_a - a_crit) / 0.02))

    # normalize color of each point to its maximum component
    rgb = np.vstack([red, green, blue])
    rgb /= np.max(rgb, axis=0)

    # return an array of RGB colors, which is shape (n_points, 3)
    return rgb.T


#------------------------------------------------------------
# Fetch data, extract the desired quantities, dither colours,
# precise only to 0.01
data = pd.read_csv('data/asteroid-belt.csv')
nrows = data.shape[0]
mag_a = data['mag_a'] - 0.005 + 0.01 * np.random.random(size=nrows)
mag_i = data['mag_i'] - 0.005 + 0.01 * np.random.random(size=nrows)
mag_z = data['mag_z'] - 0.005 + 0.01 * np.random.random(size=nrows)
a = data['aprime']
sini = data['sin_iprime']

# compute RGB color based on magnitudes
color_manual = compute_color(mag_a, mag_i, mag_z)

#------------------------------------------------------------
# set up the plot
with plt.style.context('dark_background'):
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=300)
    ax0.scatter(mag_a, mag_i - mag_z, c=color_manual, s=0.25, linewidth=0)

    ax0.set_xlabel('Optical Colour (a*)')
    ax0.set_ylabel('Near-IR Colour (i - z)')

    # plot the orbital parameters plot
    ax1.scatter(a, sini, c=color_manual, s=0.25, linewidth=0)
    ax1.set_xlabel('Distance from the Sun (AU)')
    ax1.set_ylabel('Orbital Inclination (Sine)')

    # Saving the black-background figure requires some extra arguments:
    fig.savefig('_images/asteroids.png', dpi=300)

plt.show(block=True)
