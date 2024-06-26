class Node:
	def __init__(self, id:int, isAvailable:bool, start:int, length:int, next:'Node'=None):
		self.id = id
		self.isAvailable = isAvailable
		self.start = start
		self.length = length
		self.next = next
	
	def __ge__(self, length:int)->bool:
		return self.isAvailable and self.length > length
	
	def __eq__(self, node:'Node')->bool:
		return self.id == node.id
	
	def __str__(self)->str:
		return f'{self.id}:({self.isAvailable}, {self.start}[{self.length}])'
	
	
	@staticmethod
	def smaller_start(n1:"Node", n2:"Node")->bool:
		return n1.start < n2.start
	
	@staticmethod
	def smaller_length(n1:"Node", n2:"Node")->bool:
		return n1.length < n2.length