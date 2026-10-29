# %%
import numpy as np
import matplotlib.pyplot as plt

import sys
repo_path = '/n/home02/amphillips/petar_tutorial'
sys.path.append(repo_path+'/include/') #<--add include directory to the pythonpath. this has worked on my laptop, where petar itself is not actually installed. but if you're in an environment where petar is installed anyway you don't need this. 
import petar
import astropy.units as u
# %%
# load tidal data: 
tidal = petar.Tidal()

orbit='gd1' #<'circ','gd1','pa5'
rvir='6' #<--'0.75','3','6'
tidal.loadtxt(repo_path+'/data/%s/rvir%s/data.tidal'%(orbit, rvir))

fig, axs = plt.subplots(4, 1, figsize=[6,12])
yvals = [tidal.n,    
         tidal.rtid, # pc
         tidal.mass, # Msun
         tidal.pot   # pc^2 / Myr^2
         ]
labels = [r"$N_{\rm bound}$", r"$R_{\rm tid}~[\rm pc]$", r"$M_{\rm bound}~[M_{\odot}]$", r"$\Phi_{\rm ext}~[\rm pc^2 ~Myr^{-2}]$"]
for ii, y in enumerate(yvals):
    axs[ii].plot(tidal.time,  y)
    axs[ii].set_ylabel(labels[ii])

axs[-1].set_xlabel(r't (Myr)')

plt.savefig("plots/tidal_demo.pdf", dpi=300, bbox_inches='tight')
# %%
#--------------- load and plot the core position---------#
core = petar.Core()
core.loadtxt(repo_path+'/data/%s/rvir%s/data.core'%(orbit, rvir))

x,y,z = core.pos.T * u.pc.to(u.kpc)
vx, vy, vz = core.vel.T * (u.pc/u.Myr).to(u.km/u.s)

fig, axs = plt.subplots(1, 3, figsize=[18,5])

axs[0].plot(x,y)
axs[0].scatter(x[-1], y[-1], c='y', edgecolor='k', lw=1, s=500, marker='*')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

axs[1].plot(x,z)
axs[1].scatter(x[-1], z[-1], c='y', edgecolor='k', lw=1, s=500, marker='*')
axs[1].set_xlabel('x')
axs[1].set_ylabel('z')


axs[2].plot(y,z)
axs[2].scatter(y[-1], y[-1], c='y', edgecolor='k', lw=1, s=500, marker='*')
axs[2].set_xlabel('y')
axs[2].set_ylabel('z')
plt.savefig("plots/core_orbit.pdf")
# %%