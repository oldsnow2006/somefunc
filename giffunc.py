from tkinter import *
import time
import os
root = Tk()


numIdx = 6 # gif的帧数
frames = []
for i in range(6):
	frame=PhotoImage(file='gif002.gif',format='gif -index '+str(i))
	frames.append(frame)



def update(idx):
	frame = frames[idx]

	
	label.configure(image=frame)
	idx += 1
	if idx==numIdx:
		idx=0	
	root.after(200, update, idx)


label = Label(root,bg='white')
label.pack()
root.after(0, update, 0)
root.mainloop()