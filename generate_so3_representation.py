from random import uniform
from numpy import arccos, pi, array, cos, sin, cross, sqrt

from sympy.abc import a,b
from sympy import Matrix
from itertools import product
from sympy.physics.quantum import TensorProduct

# A \otimes \rho_{d}
def orderedTensorProduct(d):
	dDegreeMonomials = monomialDegrees(d)
	xyz = monomialDegrees(1)
	retVal = []
	for x in xyz:
		retVal.extend([ (a[0] + b[0], a[1] + b[1], a[2] + b[2]) for (a, b) in product([x], dDegreeMonomials) ])
	return retVal

# sort monomials in x & y above those that contain a z. Within these two groups sort lexically and by degree. 
def homogenousMonomialOrdering(monomials,d):
	return sorted(monomials, key=lambda x: (x[2], x[1]))

def monomialDegrees(d):
	retVal =[]
	for (i,j,k) in product(list(range(d+1)), repeat=3):
		if( i + j + k == d):
			retVal.append((i,j,k))
	return homogenousMonomialOrdering(retVal,d)

def makeProjection(pd_basis, quotient_basis):
	retVal = []
	for hm in pd_basis:
		retVal.append([1 if tup == hm else 0 for tup in quotient_basis])
		
	return Matrix(retVal)

def makeEmbedding(pd_basis, quotient_basis):
	retVal      = []
	qb_length   = len(quotient_basis)

	for hm in pd_basis:
		ret = []
		count = 0 
		for idx in range(qb_length-1,-1,-1):
			if (count == 0 and quotient_basis[idx] == hm):
				ret.insert(0,1)
				count += 1
			else: 
				ret.insert(0,0)
		retVal.append(ret)
	return Matrix(retVal).transpose()

def produceProjectionAndEmbedding(degree):
	pd_basis = monomialDegrees(degree)
	quotient_basis = orderedTensorProduct(degree - 1)
	return makeProjection(pd_basis, quotient_basis), makeEmbedding(pd_basis, quotient_basis)

def representationOfSO3(A, degree):
	rho = A
	if (degree == 1):
		return A

	for i in range(2,degree+1):
		S, E = produceProjectionAndEmbedding(i)
		rho = S * TensorProduct(A,rho) * E

	return rho

# generate a random SO(3) matrix.
# return a rotation around a randomly generated axis, as 
# well as the axis
def generateSO3():
    # generate equally likely azimuth/elevation pair
    # on the upper hemisphere.
    phi   = 2 * pi * uniform(0, 1)
    theta = arccos(1 - 2 * uniform(0, 0.5))

    # axis of rotation
    axis = array([cos(phi) * sin(theta), sin(phi) * sin(theta), cos(theta)], float)
    xp   = array([cos(phi) * cos(theta), sin(phi) * cos(theta), -sin(theta)], float)
    yp   = array([-sin(phi), cos(phi), 0])
    return Matrix([xp, yp, axis]).transpose(), axis

    # We imagine z-axis => axis
    #
    #
    #
    # Solve for 'p'
    # z = (z.dot(p)) * p + (z.dot(axis)) * axis
    #   = p[2] * p + axis[2] * axis
    #
    #  w = p[2] * p = (p[2] * p[0], p[2] * p[1], p[2] * p[2])
    #w = array([0,0,1], float) - axis[2] * axis
    #p = w / sqrt(w[2])
    #return Matrix([cross(axis, p), -p, axis]).transpose(), axis
