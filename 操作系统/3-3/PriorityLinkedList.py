from Node import Node
from typing import Callable

class PriorityLinkedList:
	def __init__(self, totalLength:int=1024, order:Callable[[Node,Node],bool]=Node.smaller_start, copy:"PriorityLinkedList"=None, decopy:"PriorityLinkedList"=None):
		if copy is None:
			if decopy is None:
				self.next = Node(0, True, 0, totalLength)
				self.order = order
			else:
				cur = decopy.next
				self.next = Node(cur.id, cur.isAvailable, cur.start, cur.length)
				self.order = order
				
				cur = cur.next
				while cur is not None:
					self.insert(Node(cur.id, cur.isAvailable, cur.start, cur.length))
					cur = cur.next
		else:
			cur = copy.next
			self.next = Node(cur.id, cur.isAvailable, cur.start, cur.length)
			self.order = Node.smaller_start
			
			cur = cur.next
			while cur is not None:
				self.insert(Node(cur.id, cur.isAvailable, cur.start, cur.length))
				cur = cur.next


	def insert(self, newNode:Node)->None:
		if newNode.length > 0:
			prev, cur = self, self.next
			while cur is not None:
				if self.order(newNode, cur):
					prev.next, newNode.next = newNode, cur
					return
				prev, cur = cur, cur.next
			
			prev.next, newNode.next = newNode, None
		return
	

	def delete(self, node:Node)->bool:
		prev, cur = self, self.next
		while cur is not None:
			if cur == node:
				prev.next = cur.next
				return True
			prev, cur = cur, cur.next

		return False


	def print(self)->int:
		count = 0
		cur = self.next
		print("head")
		while cur is not None:
			print("-> " + str(cur))
			cur = cur.next

			count += 1

		print("-> None\n")
		return count

			


