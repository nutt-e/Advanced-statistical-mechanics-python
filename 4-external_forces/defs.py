import numpy


kT=4.1				#room temperature, pN nm
zeta=20				#friction in pN us/nm.  1um sphere in water.
m=0.21				#mass in pg.  This is a polystyrene bead of radius 1um
dt=0.02				#timestep in us
nstep=10000			#number of steps to perform


USEBROWNIAN=True


USELANGEVIN=False
if USEBROWNIAN:
	brownianVariance=numpy.sqrt(2*kT*dt/zeta);
	brownianFactor=dt/zeta;
else:
	USELANGEVIN=True
	langevinVariance=numpy.sqrt(2*kT*zeta/dt)
	langevinFactor1=(1-zeta*dt/2/m)/(1+zeta*dt/2/m)
	langevinFactor2=dt*dt/m/(1+zeta*dt/2/m)

