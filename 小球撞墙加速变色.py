from tkinter import *
import time
import random
class Ball(object):
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,random.choice(range(100,300)),random.choice(range(100,300)))
        a=[-1,-2,-3,1,2,3]
        self.x=random.choice(a)
        self.y=random.choice(a)
        self.color1=['blue','green','red','black','yellow','pink','purple','orange']
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.canvas.itemconfig(self.id,fill=random.choice(self.color1))
            self.y=self.y*-1.1
        if pos[3]>=self.canvas.winfo_height():
            self.y=self.y*-1.1
            self.canvas.itemconfig(self.id,fill=random.choice(self.color1))
        if pos[0]<=0:
            self.x=self.x*-1.1
            self.canvas.itemconfig(self.id,fill=random.choice(self.color1))
        if pos[2]>=self.canvas.winfo_width():
            self.x=self.x*-1.1
            self.canvas.itemconfig(self.id,fill=random.choice(self.color1))
            
if __name__=='__main__':
    tk=Tk()
    tk.title('tast')
    tk.resizable(0,0)
    tk.wm_attributes('-topmost',1)
    tk.wm_attributes('-alpha',0.7)
    canvas=Canvas(tk,width=500,height=500)
    canvas.pack()
    ball1=Ball(canvas,'red')
    ball2=Ball(canvas,'red')
    ball3=Ball(canvas,'red')
    ball4=Ball(canvas,'red')
    ball5=Ball(canvas,'red')
    while 1:
        ball1.draw()
        ball2.draw()
        ball3.draw()
        ball4.draw()
        ball5.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)