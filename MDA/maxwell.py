import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import Plots
import Student

# Set up the simulation parameters
# box_size = 10.0 # Angstroms
# n_atoms = 100
# time_step = 0.01 # picoseconds
temperature = 900 # Kelvin
# sampling_interval = 100 # Number of time steps between velocity sampling
# sampling_time = 1000 # Time at which to sample velocities (in picoseconds)


argon = mda.Universe("trj.lammpsdump", atom_style='id type x y z ix iy iz vx vy vz')
selection = argon.select_atoms('all')
selection.masses = 39.948

# Print the number of selected atoms
print("Number of atoms:", len(selection))
print("Number of frames:", len(argon.trajectory))


# Generate initial coordinates and velocities

# Run the simulation
# Use your preferred MD simulation package to run the simulation, and output a trajectory file in a format that can be read by MDAnalysis
# Sample velocities and histogram




mass = (selection.masses.sum() / (len(selection) * 6.02)) * 10 ** (-26)


def maxwell_boltzmann(v, A, alpha):
    global temperature, mass
    T = temperature
    m = mass
    k_B = 1.380649e-23 # Boltzmann constant in J/K
    return A * (m / (2 * np.pi * k_B * T)) ** (3/2) * 4 * np.pi * v**2 * np.exp(-alpha * m * v**2 / (2 * k_B * T))

def normal(v, A, alpha):
    global temperature, mass
    T = temperature
    m = mass
    k_B = 1.380649e-23 # Boltzmann constant in J/K
    return A * (m / (2 * np.pi * k_B * T)) ** (3/2) * np.exp(- alpha * m * v**2 / (2 * k_B * T))

popts = []

for ts in argon.trajectory[-10:-1]:
    velocities_list = []
    velocities_list.append(ts.velocities.copy())
    velocities_array = np.concatenate(velocities_list)
    velocities_array = velocities_array * 100
    velocities_norm = np.linalg.norm(velocities_array, axis=1)
    velocities_hist, bin_edges = np.histogram(velocities_norm, bins=60, density=True)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    popt, pcov = curve_fit(maxwell_boltzmann, bin_centers, velocities_hist, p0=[1, 1])
    popts.append([*popt])

arr_A = np.array([sub[0] for sub in popts], dtype=float)
arr_alpha = np.array([sub[1] for sub in popts], dtype=float)

popt = [np.mean(arr_A), np.mean(arr_alpha)]
print("Means", *popt)
print("Stds: ", np.std(arr_A, ddof=1), np.std(arr_alpha, ddof=1))

# # Plot the distribution and the fitted curve
plt.plot(bin_centers, velocities_hist, 'o', label='simulation')
plt.plot(bin_centers, maxwell_boltzmann(bin_centers, *popt), label='fit')
plt.xlabel("A = {}, alpha = {}".format(*popt))
plt.title("Maxwell-Boltzmann distribution for Argon, T: {}, N: {}".format(temperature, len(selection)))
plt.legend()
plt.show()


# # print(velocities_list)


# # # Fit the Maxwell-Boltzmann distribution to the data







# # Print the parameters of the fitted distribution
# print('Temperature: {:.2f} K'.format(popt[0]))
# print('Mass: {:.2f} amu'.format(popt[1]))
