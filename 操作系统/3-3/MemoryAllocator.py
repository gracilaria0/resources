from PriorityLinkedList import PriorityLinkedList
from Node import Node

class MemoryAllocator:
	def __init__(self, mode:str="best", totalLength:int=1024):
		self.count = 0
		self.totalLength = totalLength
		self.mode = mode
		if self.mode == "best":
			self.list = PriorityLinkedList(totalLength, Node.smaller_length)
		elif self.mode == "worst":
			self.list = PriorityLinkedList(totalLength, lambda n1, n2: not Node.smaller_length(n1, n2))
		else:
			self.list = PriorityLinkedList(totalLength, Node.smaller_start)
		self.pointer = self.list
		if self.mode == "next":
			self.initPosition = self.list

	def _pointerInit(self)->Node:
		self.count += 1
		if self.mode == "next":
			return self.pointer
		self.pointer = self.list
		self.initPosition = self.pointer
		return self.pointer

	def _pointerPulsplus(self)->Node:
		self.count += 1
		self.pointer = self.pointer.next
		if self.mode == "next" and self.pointer is None:
			self.pointer = self.list
		return self.pointer
	
	def _endCondition(self)->bool:
		self.count += 1
		if self.mode == "next":
			if type(self.initPosition) == PriorityLinkedList:
				return False
			if self.initPosition.next is None:
				self._pointerPulsplus()
			return  self.initPosition == self.pointer.next
		return self.pointer.next is None
	
	def startList(self)->PriorityLinkedList:
		self.count += 1
		return PriorityLinkedList(copy=self.list)
	
	def printList(self, mode:str="start")->int:
		self.count += 1
		if mode == "start":
			temp = self.startList()
			return temp.print()
		else:
			return self.list.print()
	

	def allocate(self, length:int) -> None:
		print(f"Requesting for {length}\n")
		if length > self.totalLength:
			raise ValueError("Length is greater than total length of memory")
		
		self._pointerInit()
		while not self._endCondition():
			if self.pointer.next >= length:
				cur = self.pointer.next
				self.list.delete(self.pointer.next)
				self.list.insert(Node(self.count, False, cur.start, length))
				self.list.insert(Node(self.count+1, True, cur.start + length, cur.length - length))
				break
			self._pointerPulsplus()
		else:
			raise ValueError("Memory is not enough to allocate")
		
	
	def _smooth(self)->None:
		self.count += 1
		temp = self.startList()
		changeFlag = True
		while changeFlag:
			changeFlag = False
			prev, cur = temp.next, temp.next.next
			while cur is not None:
				if cur.isAvailable and prev.isAvailable:
					temp.delete(prev)
					temp.delete(cur)
					temp.insert(Node(self.count, True, prev.start, prev.length + cur.length))
					changeFlag = True
					break
				prev, cur = cur, cur.next

		self.list = PriorityLinkedList(order=self.list.order, decopy=temp)
		

	def deallocate(self, id:int) -> None:
		self.count += 1
		print(f"Deleting Allocation with id {id}\n")
		cur = self.list.next
		while cur is not None:
			if cur.id == id:
				self.list.insert(Node(self.count, True, cur.start, cur.length))
				break
			cur = cur.next
				
		if not self.list.delete(Node(id, True, 0, 0)):
			raise ValueError("Allocation with given id not found")
		
		self._smooth()
		
		