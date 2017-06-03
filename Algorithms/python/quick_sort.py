#!/usr/bin/python
# -*- coding: utf-8 -*-
import util
from util import LIST
EXCHANGE = util.EXCHANGE

import random

#good: 
# good average time cost, with small factor of nlg(n)
# origin addr sort
#bad:
# bad worst time complexity, O(n2)


#A[p..r] -> A[p..q-1], A[q+1..r]
#O(n)
def PARTITION(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i += 1
			A[i],A[j] = EXCHANGE(A[i],A[j])
	A[i+1],A[r] = EXCHANGE(A[i+1],A[r])
	return i + 1

# O(n)xn = O(n2)
def QUICK_SORT(A, p, r):
	if(p < r):
		q = PARTITION(A, p, r)
		QUICK_SORT(A, p, q-1)
		QUICK_SORT(A, q+1, r)


#
# random-sampled quicksort
#


def RANDOMIZED_PARTITION(A, p, r):
	i = random.randint(p, r)
	A[r], A[i] = EXCHANGE(A[r], A[i])
	return PARTITION(A, p, r)

def RANDOMIZED_QUICKSORT(A, p, r):
	if(p < r):
		q = RANDOMIZED_PARTITION(A, p, r)
		RANDOMIZED_QUICKSORT(A, p, q-1)
		RANDOMIZED_QUICKSORT(A, q+1, r)


if __name__ == "__main__":
	print "START"
	Array = [1, 3, 2, 4,111,32,321,42,16,37]
	A = LIST(Array)
	#QUICK_SORT(A,0,9)
	RANDOMIZED_QUICKSORT(A, 0, 9)
	A.display()


