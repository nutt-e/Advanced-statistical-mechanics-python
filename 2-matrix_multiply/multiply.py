import numpy as np;  #numpy is generally useful for scientific computing
from numpy.linalg import matrix_power;  #maxtrix power is not included by default when 
										#importing numpy, so we need to include it as well.
										#this function computes the matrix power far
										# more efficiently than our C code.  

import datetime as dt;  #this lets us keep track of time




n=50;  #matrix size
m=20;  #power to raise the matrix by


def simpleMultiply(mat1,mat2,tmp):  #this defines a function to do the simple multiplication.
									#python's notation is much easier than C++.

	for i in range(n):				
		for j in range(n):			#iterate over the matrix elements i and j
			tmp[i,j]=0;
			for k in range(n):
				tmp[i,j]+=mat1[i,k]*mat2[k,j];  #update the temp matrix
	for i in range(n):
		for j in range(n):
			mat2[i,j]=tmp[i,j];					#save the updated matrix
			
			
			

oldmat=np.random.rand(n,n)  #generate a random matrix
for i in range(n):
	oldmat[i]/=np.sum(oldmat[i]);  	#normalize the rows like we did in C
newmat=np.identity(n); 				#generate an identity matrix
tmpmat=np.zeros((n,n));				#get a temp matrix of zeros



t0 = dt.datetime.now()				#define the current time to determine time intervals
matrix_power(oldmat,m);				#this uses python's efficient algorithm to get the matrix power
tf=dt.datetime.now();				#check how long it took.
print((tf-t0).total_seconds()*1000," ms passed for simple matrix_power");



t0 = dt.datetime.now()
for iter in range(m):
	simpleMultiply(oldmat,newmat,tmpmat);	#this uses our less efficient product method.  
											#this is the simpler implementation, and is
											#identical to what we did in C++
tf = dt.datetime.now()
print((tf-t0).total_seconds()*1000," ms passed for simple multiply");



