### demo for petar tidal and core files


see use in `use_tidal_and_core_data.py`

Data are in the `/circ`,`/gd1`,`/pa5` directories (corresponding to orbits). Within each orbit directory, select clusters of different densities -- fixed N=15k, initial virial radii 0.75, 1.5, 3.0, 6.0 pc. 

`/include` has the python analysis portion of `petar` in case you haven't completed the full install (once the data is processed you really only need these for easy/automatic loading of the files). 

sims are run in Bovy MW 2014, with initial displacements (x,y,z,vx,vy,vz) in pc, km/s

```
circular orbit: (20000.0, 0.0, 0.0, 0.0, 197.61111175113643, 0.0)
gd-1 orbit: (-14680.175269960177, -18049.00342055592, -3355.258112269282,126.94017915235732, -33.56076783776999, 112.93136486685516)
pal 5 orbit: (13536.852506889449, -3328.304203161837, 5478.0923546972035,119.95920838380918, -89.0209982268969, -88.31131556786855)
```

for GD-1 and pal 5 the initial displacements are defined so that at 10 Gyr the integrated progenitor orbit matches the present day location (see phillips+26 for references). 

You can re-integrate the progenitor orbit given these ICs in gala or agama or whatever. However, the enclosed mass/number of particles within rtid is calculated in post-processing using their distance from the simulation's _core_ or density peak. For various reasons the core drifts from the location of the progenitor as integrated as a non-interacting test particle (stellar evolution-related effects, differential tidal torques, etc), so if re-computing rtid yourself, best to use the position of the core and not the integrated progenitor orbit to determine the local tidal field. If you end up wanting the full particle data snapshot files I'm happy to also share a snippet of code I wrote a while ago to try and track escapers.

---

units in petar outputs tend to be:

position - pc
velocity - pc/myr
mass - Msun
potential - pc^2 / Myr^2

---
