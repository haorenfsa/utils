#!/usr/bin/python
# -*- coding: utf-8 -*-
import util
from util import EXCHANGE, LIST
EXCHANGE = util.EXCHANGE

#以下复杂度为O(1)
def PARENT(i):
	return int((i-1)/2)

def LEFT(i):
	return 2*(i+1)-1

def RIGHT(i):
	return 2*(i+1)

#维护堆的性质
#输入： 数组A，下标i
#假设 左右子树都是最大堆，但A[i]可能小于它的孩子
#递归式：T(n) <= T(2/3n) + O(1)  (每个孩子的子树大小最大为2/3n)

#关于2/3n的计算方法： 由堆的整理过程，最坏情况是最下层，左边刚满，右边没有。
#假设左子树此时为i+1层满，则右子树只有i层满
#总数求和 左边：2^x+1 x从1~i， 右边:2^x
#等比级数求和， 右/左 = 2^x-1/2^(x+1)-1
#这个函数是递减的，所以对x->正无穷，求极限可以得到函数的下界 1/2，那么左比总就是2/3
def MAX_HEAPIFY(A, i):
	l = LEFT(i)
	r = RIGHT(i)

	largest = i
	#print A.heap_size

	if l < A.heap_size:
		if A[l] > A[i]:
			largest = l

	if r < A.heap_size:
		if A[r] > A[largest]:
			largest = r

	#print largest
	if largest != i:
		A[i],A[largest] = EXCHANGE(A[i],A[largest])
		MAX_HEAPIFY(A, largest)

def BUILD_MAX_HEAP(A):
	A.heap_size = A.length
	for i in range( int((A.length-1)/2), -1, -1):
		#print i
		MAX_HEAPIFY(A,i)

def HEAP_SORT(A):
	BUILD_MAX_HEAP(A)
	for i in range(A.length-1, 0, -1):#0~9，length 10, 9~1
		#print i
		A[i],A[0] = EXCHANGE(A[i],A[0])
		A.heap_size -= 1
		MAX_HEAPIFY(A, 0)

#Z最大优先队列
#由于堆在插入时，键值调整时的复杂度低
def HEAP_MAXIMUM(A):
	return A[0]

#头尾交换后，维护最大堆
#O(lgn)
def HEAP_EXTRACT_MAX(A):
	if A.heap_size < 1:
		print "heap over flow"
		return -1
	max_var = A[0]
	A[0] = A[A.heap_size - 1]
	A.heap_size -= 1
	MAX_HEAPIFY(A, 0)
	return max_var

#每次与父节点比较
#O(lgn)
def HEAP_INCREASE_KEY(A, i, key):
	if key < A[i]:
		print "new key smaller than current"
		return -1
	A[i] = key
	while i > 0 and A[PARENT(i)] < A[i]:
		A[i],A[PARENT(i)]= EXCHANGE(A[i], A[PARENT(i)])
		i = PARENT(i)

def MAX_HEAP_INSERT_KEY(A, key):
	A.heap_size +=1
	A[A.heap_size - 1] = - 1 #应该是一个负无穷，但是我们假设堆都是正数
	HEAP_INCREASE_KEY(A, A.heap_size-1, key)


if __name__ == "__main__":
	print "START"
	Array = [1, 3, 2, 4,111,32,321,42,16,37]
	A = LIST(Array)
	BUILD_MAX_HEAP(A)
	#HEAP_SORT(A)
	print "origin"
	A.display()
	print "extract:", HEAP_EXTRACT_MAX(A)
	A.display()
	print "insert", 321
	MAX_HEAP_INSERT_KEY(A, 321)
	A.display()

