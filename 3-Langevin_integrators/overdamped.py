import numpy

kT=4.1				#room temperature, pN nm
zeta=20				#friction in pN us/nm.  1um sphere in water.
dt=0.02				#timestep
nstep=1000			#number of steps to perform

def externalForce(position):
	return 0;
	
outfile=open("trajectory_overdamped.txt","w");

x0=0				#initial position of the particle
x=x0				#current position of the particle
t=0					#current time
numpy.random.seed(1)		
					#choose a random seed.  If you delete this line,
					#the random number generator will produce a different
					#seed on each run.  

for step in range(nstep):
	f=externalForce(x)		#external force
	x+=f/zeta*dt			#update the position based on the external force
	x+=numpy.sqrt(2*kT*dt/zeta)*numpy.random.normal(0,1)
							#update the position based on the random force
	t=step*dt				#update the time
	outfile.write(repr(t)+","+repr((x-x0)*(x-x0))+"\n")
	
outfile.close()