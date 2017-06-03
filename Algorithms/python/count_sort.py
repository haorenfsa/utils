#!/usr/bin/python
# -*- coding: utf-8 -*-

import util
from util import LIST
EXCHANGE = util.EXCHANGE

# condition:
# all input is from 0~k
# when k = O(n), this algo is O(n)

#
# A is input, B is output(must be init)
# C is tmp space
#
def COUNTING_SORT(A, B, k):
    C = LIST({})
    for i in range(k+1):
        C[i] = 0

    for j in range (A.length):
        C[A[j]] = C[A[j]] + 1

    #C[i] now  contains the number of elements equal to i

    for i in range(1,k+1):
        C[i] = C[i] + C[i - 1]

    #C[i] now  contains the number of elements less than or equal to i

    # A.length-1 downto 0
    for j in range(A.length-1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1


if __name__ == "__main__":
    print "START"
    Array = [1, 3, 2, 4,111,32,321,42,16,37]
    A = LIST(Array)
    B = LIST([None]*10})
    COUNTING_SORT(A, B, 321)
    B.display()
