#workflow to run this test for cython:  
#	python3 setup.py build_ext --inplace
#	python3
# 	import integrators

import numpy
import cython

cdef float kT=4.1				#room temperature, pN nm
cdef float zeta=20				#friction in pN us/nm.  1um sphere in water.
cdef float m=0.21				#mass in pg.  This is a polystyrene bead of radius 1um
cdef float dt=0.02				#timestep in us
cdef int nstep=1000			#number of steps to perform

cdef float externalForce(x):
	return 0;
	

cdef (float,float) langevinIntegration(x,xold):
	cdef float f,R,xnew
	f=externalForce(x)		#external force
	R=numpy.sqrt(2*kT*zeta/dt)*numpy.random.normal(0,1)
							#random force.  Note that the factor in the 
							#sqrt is different than for brownian motion.  
	xnew=x
	xnew+=(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m)	#velocity term
	xnew+=(f+R)*dt*dt/m/(1+zeta*dt/2/m)				#acceleration term
	xold=x;
	x=xnew;
	return x,xold
	

cdef float overdampedIntegration(x):
	cdef float f,R
	f=externalForce(x)		#external force
	R=numpy.sqrt(2*kT*dt/zeta)*numpy.random.normal(0,1)
	x+=f/zeta*dt+R
	return x




cdef float x0=0				#initial position of the particle
cdef float xold=x0				#previous position of the particle
cdef float x=x0				#current position of the particle
cdef float xnew=x0				#new position of the particle
cdef float t=0					#current time
numpy.random.seed(1)		
					#choose a random seed.  If you delete this line,
					#the random number generator will produce a different
					#seed on each run.  




cdef int step

outfile=open("trajectory_langevin.txt","w");
for step in range(nstep):
	x,xold=langevinIntegration(x,xold)
	outfile.write(repr(step*dt)+","+repr((x-x0)*(x-x0))+"\n")
outfile.close()

outfile=open("trajectory_overdamped.txt","w");
for step in range(nstep):
	x=overdampedIntegration(x)
	outfile.write(repr(step*dt)+","+repr((x-x0)*(x-x0))+"\n")
outfile.close()