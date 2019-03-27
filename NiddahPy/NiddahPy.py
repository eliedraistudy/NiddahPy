#!/usr/bin/env

from enum import Enum
from dates import *

class Onah(Enum):
	Night = 1
	Day = 2

class Flow(object):
	"""
	A class to describe the date of the first flow
	Also describe the Onah
	"""
	
	def __init__(self, date, onah):
		"""
		Constructor for the flow descriptor
		"""
		self.date = date
		self.onah = onah
		
	def __str__(self):
		"""
		To string method for Flow
		"""
		onah = str(self.onah)
		return "Flow date: {d}\tOnah: {o}".format(d=str(self.date), o=onah)
	
	@classmethod
	def OnahBenonis(self):
		"""
		Give the next date for onah benonis
		"""
		return self.date + 30
	
	@classmethod
	def OnahHodesh(self):
		"""
		Give the next date for onah hahodesh
		"""
		
	@classmethod
	def TODO(self):
		"""
		Gives what to do for this flow
		"""
		
		


