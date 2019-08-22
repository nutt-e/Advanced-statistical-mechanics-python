#workflow to run this test for cython:  
#	python3 setup.py build_ext --inplace
#	python3
# 	import test

import datetime as dt  #this lets us keep track of time
cimport cython  #required to use cython
import numpy as np # build arrays
import random  #generate random numbers
from numpy.linalg import matrix_power


cdef int n=500	#array size
cdef int m=20	#power to use

def runtest():		#this is a python implementation that will call the cython-y code
	cdef int iter
	for iter in range(m):
		speedtest_c(c_old,c_new,c_tmp)


cdef void speedtest_c(float[:,:] mat1,float[:,:] mat2, float[:,:] tmp):  #this is the simpleminded way to multiply a matrix
	cdef int i,j,k					# remember to type EVERYTHING in order to get the speed boost.  
	for i in range(n):				
		for j in range(n):			#iterate over the matrix elements i and j
			tmp[i,j]=0;
			for k in range(n):
				tmp[i,j]+=mat1[i,k]*mat2[k,j];  #update the temp matrix
	for i in range(n):
		for j in range(n):
			mat2[i,j]=tmp[i,j];					#save the updated matrix






#Generate numpy array:
oldmat = np.zeros((n,n), dtype=np.dtype("f"))		#start by defining our matrices as a type float (the "f");
newmat = np.zeros((n,n), dtype=np.dtype("f"))		#note that using just dtype does not cause the fast c-type
tmpmat = np.zeros((n,n), dtype=np.dtype("f"))		#speedup.  All matrices initially at zero.

cdef int i, j			#we're looping over integers, so be sure to type them in cython
for i in range(n):
	newmat[i][i]=1.0;	#newmat is the identity matrix:  ones on diagonal, zeros other.
	for j in range(n):
		oldmat[i][j]=random.random()		#put a random number in each element of the old matrix
for i in range(n):
	oldmat[i]/=np.sum(oldmat[i]);  	#normalize the rows of the old matrix


t0 = dt.datetime.now()				#define the current time to determine time intervals
builtIn=matrix_power(oldmat,m);				#this uses python's efficient algorithm to get the matrix power
tf=dt.datetime.now();				#check how long it took.
print((tf-t0).total_seconds()*1000," ms passed for simple matrix_power");
print(builtIn)
print("\n")


cdef float [:,:] c_old=oldmat;		#this defines c-like arrays in cython.
cdef float [:,:] c_new=newmat;		#I believe this copies each array, so this is less efficient
cdef float [:,:] c_tmp=tmpmat;		#memory-wise.  It is likely you can cleverly get around this inefficiency.




t0 = dt.datetime.now()				#define the current time to determine time intervals
runtest()							#compute the matrix power
tf = dt.datetime.now()				#figure out the current time
print((tf-t0).total_seconds()*1000," ms passed for simple multiply using cython");

finished=np.asarray(c_new)			#convert the c-like array into a numpy array
print(finished)						#print the data as a sanity check
