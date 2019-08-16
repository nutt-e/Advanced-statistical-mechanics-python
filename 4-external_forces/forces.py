from defs import *
import numpy

def externalForce(x,y):
	rsq=x*x+y*y
	fx=20*x-4*x*rsq
	fy=20*y-4*y*rsq
	return fx,fy


def overdamped(x,y,fx,fy):
	Rx=brownianVariance*numpy.random.normal(0,1)
	Ry=brownianVariance*numpy.random.normal(0,1)
	x+=fx*brownianFactor+Rx
	y+=fx*brownianFactor+Ry					
	return x,y
	#typo on purpose here...
	
def langevin(x,y,xold,yold,fx,fy):
	Rx=langevinVariance*numpy.random.normal(0,1)
	Ry=langevinVariance*numpy.random.normal(0,1)
	xnew=x+(x-xold)*langevinFactor1+(fx+Rx)*langevinFactor2
	ynew=y+(y-yold)*langevinFactor1+(fy+Ry)*langevinFactor2
	xold=x
	yold=y
	x=xnew
	y=ynew
	return x,y,xold,yold
	
	


x0=0			#initial position of the particle
xold=x0				#previous position of the particle
x=x0				#current position of the particle
y0=0;
yold=y0;
y=y0;			
fx=0;
fy=0;


numpy.random.seed(1)		

if USEBROWNIAN:
	outfile=open("trajectory_overdamped.txt","w")
if USELANGEVIN:
	outfile=open("trajectory_langevin.txt","w")

for step in range(nstep):
	fx,fy=externalForce(x,y)
	if USEBROWNIAN:
		x,y=overdamped(x,y,fx,fy);
	if USELANGEVIN:
		x,y,xold,yold=langevin(x,y,xold,yold,fx,fy)
	t=step*dt				
	outfile.write(repr(t)+","+repr(x)+","+repr(y)+"\n")

outfile.close()