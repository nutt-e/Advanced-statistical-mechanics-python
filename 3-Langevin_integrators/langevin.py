import numpy

kT=4.1				#room temperature, pN nm
zeta=20				#friction in pN us/nm.  1um sphere in water.
m=0.21				#mass in pg.  This is a polystyrene bead of radius 1um
dt=0.02				#timestep in us
nstep=1000			#number of steps to perform

def externalForce(x):
	return 0;
	
outfile=open("trajectory_langevin.txt","w");

x0=0				#initial position of the particle
xold=x0				#previous position of the particle
x=x0				#current position of the particle
xnew=x0				#new position of the particle
t=0					#current time
numpy.random.seed(1)		
					#choose a random seed.  If you delete this line,
					#the random number generator will produce a different
					#seed on each run.  

for step in range(nstep):
	f=externalForce(x)		#external force
	R=numpy.sqrt(2*kT*zeta/dt)*numpy.random.normal(0,1)
							#random force.  Note that the factor in the 
							#sqrt is different than for brownian motion.  
	xnew=x
	xnew+=(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m)	#velocity term
	xnew+=(f+R)*dt*dt/m/(1+zeta*dt/2/m)				#acceleration term
	t=step*dt				#update the time
	xold=x;
	x=xnew;
	outfile.write(repr(t)+","+repr((x-x0)*(x-x0))+"\n")
	
outfile.close()