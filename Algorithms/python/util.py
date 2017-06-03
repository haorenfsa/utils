#!/usr/bin/python
# -*- coding: utf-8 -*-
#utils
def EXCHANGE(a, b):
	return (b, a)

class LIST(object):
	def __init__(self, Array):
		self.heap_size = len(Array)
		self.data = {}
		self.length = len(Array)
		#print self.length
		for i in range(self.length):
			self.data[i] = Array[i]

	def __getitem__(self, key):
		return self.data[key]

	def __setitem__(self, key, value):
		self.data[key] = value

	def display(self):
		for i in range(self.heap_size):
			print self.data[i]