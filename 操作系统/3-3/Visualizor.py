import tkinter as tk
from MemoryAllocator import MemoryAllocator

class Visualizor(MemoryAllocator):
	def __init__(self):
		super().__init__(mode="next")

		self.window = tk.Tk()
		self.window.title("动态内存分配可视化器")
		self.window.geometry("330x200")
		self.canvasWidth, self.canvasHeight = 300, 100

		self.requestLength = tk.Entry(self.window, width=10)
		self.requestLength.place(x=100, y=150)
		self.submit = tk.Button(self.window, text="提交", command=self.submitBehavior)
		self.submit.place(x=200, y=150)
		self.delete = tk.Button(self.window, text="删除", command=self.deleteBehavior)
		self.delete.place(x=250, y=150)

		self.memMap = tk.Canvas(self.window, width=self.canvasWidth, height=self.canvasHeight, bg="white")
		self.memMap.place(x=10, y=10)
		self.drawRects()

		self.window.mainloop()


	def drawRects(self)->None:
		cur = self.startList().next
		while cur is not None:
			self.memMap.create_rectangle(self.canvasWidth*cur.start/self.totalLength, 0, self.canvasWidth*(cur.start+cur.length)/self.totalLength, self.canvasHeight, fill="green" if cur.isAvailable else "blue")
			cur = cur.next

	
	def submitBehavior(self):
		length = int(self.requestLength.get())
		self.allocate(length)
		self.printList()
		self.drawRects()

	
	def deleteBehavior(self):
		id = int(self.requestLength.get())
		self.deallocate(id)
		self.printList()
		self.drawRects()
	

app = Visualizor()