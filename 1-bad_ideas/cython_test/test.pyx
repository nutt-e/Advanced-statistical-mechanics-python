#to use cython, there are a few additiona steps.  
# pip3 install cython
# 
# create cython code, which looks like python but allows you to typedef.
# an example is below.  For this example, save it in a file "cython_test.pyx"
# 
# create a file setup.py as here
# 
# run 
#	python3 setup.py build_ext --inplace
# note that a number of auxiliary files will be created when you do this.
#
# also note that this did not run correclty on os x, I had to update my path for c:
# add the following to .bash_profile (or .bashrc) 
#	export C_INCLUDE_PATH="/System/Library/Frameworks/Python.framework/Headers:$PATH"
#	export CFLAGS="-I /usr/local/lib/python3.7/site-packages/numpy/core/include $CFLAGS"
# then 
#	source .bash_profile
#
# Now you have code that can be run.  You can just run it in a python environment:
# 		python
#		import test
# will run it.  



i=0
while True:
	if i%10000000==0:
		print(i)
	i+=1;
	if i>20000000:
		break
print("that was slow using python")


cdef int j=0
while True:
	if j%10000000==0:
		print(j)
	j+=1;
	if j>200000000:	#note:  this is 10x as many as the cutoff above
		break
print("that was fast using cython");
